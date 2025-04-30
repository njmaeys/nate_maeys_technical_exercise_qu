import os
from uuid import UUID
from datetime import datetime
from fastapi import APIRouter, Path, Query, HTTPException, Depends, Header
from collections import defaultdict

from app.db.session import SessionLocal
from app.db.controllers.controller_all import CircuitsController, OrganizationsController
from services.insights.ts_client import query
from services.insights.responses import CircuitPowerUsageResponse, CircuitPowerUsageByLocationResponse

from app.core.config import INTERNAL_API_KEY

router=APIRouter(
    tags=['insights'],
)


"""
NOTE:
I tend to use a data envelope in responses to allow for any metadata should we need it.
Meaning a reaponse would be ie;
{
    "data": [
        ... < THE DATA > ...
    ],
    "metadata": {
        ... < THE METADATA > ...
    },
}
But for simplicity and not really knowing what metatdata we may need I'm keeping route responses
striclty to the data that the consumer will need that I'm aware of.
"""

async def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != INTERNAL_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key


@router.get(
    '/circuits/{circuit_id}/power-usage',
    description="Returns the total power in watts consumed by a circuit in the requested time period.",
    response_model=CircuitPowerUsageResponse,
    dependencies=[Depends(verify_api_key)],
)
def circuits_power_usage_by_id(
    circuit_id: UUID = Path(
        title="Circuit ID",
        description="The unique circuit ID to query. Format: UUID",
    ),
    start_date_time: datetime = Query(
        default="",
        description="The timestamp to start the query at. Format example: 2024-04-01T22:00:00Z",
    ),
    end_date_time: datetime = Query(
        default="",
        description="The timestamp to end the query at. Format example: 2024-04-01T22:28:00Z",
    ),
):
    try:
        # Initialize the DB session
        session = SessionLocal()

        # Find the circuit and sensor data for the curcuit_id
        circuit_and_sensor_data = CircuitsController.get_circuits_data_by_id(
            session=session,
            circuit_id=circuit_id,
        )

        if not circuit_and_sensor_data:
            raise HTTPException(
                status_code=404,
                detail="Circuit ID not found"
            )
        
        # Pass in the appropriate circuit and sensor data for the TS data
        ts_data = query(
            duid=circuit_and_sensor_data.sensor_duid,
            circuit=circuit_and_sensor_data.circuit_number,
            start=start_date_time,
            end=end_date_time,
        )

        # Wattage consumption
        total_power_consumed = sum(ts['power_watts'] for ts in ts_data)
        average_power_consumed = round(sum(ts['power_watts'] for ts in ts_data) / len(ts_data), 5)
    except Exception as e:
        """
        NOTE: There is much better error handling to do around types of issues.
        ie; DB connection timeout, no data found, invalid parsing of datetimes, ... so on
        for simplicity I'm doing a full catch all for timeboxing to get this done.
        NOTE: Same thing on the status_code=500... I'm taking liberties with simple 500 here
        to allow myself to complete these in a timely maner and show I can handle exceptions.
        """
        raise HTTPException(
            status_code=500,
            detail=f"Server error: {e}"
        )

    return CircuitPowerUsageResponse(
        circuit_id=circuit_and_sensor_data.circuit_id,
        circuit_number=circuit_and_sensor_data.circuit_number,
        circuit_name=circuit_and_sensor_data.circuit_name,
        sensor_id=circuit_and_sensor_data.sensor_id,
        sensor_duid=circuit_and_sensor_data.sensor_duid,
        sensor_name=circuit_and_sensor_data.sensor_name,
        wattage_consumed=total_power_consumed,
        average_wattage_consumed=average_power_consumed,
    )

@router.get(
    '/organizations/{organization_id}/power-usage/location',
    description="Returns the total and average power in watts consumed per location, per circuit.",
    response_model=list[CircuitPowerUsageByLocationResponse],
    dependencies=[Depends(verify_api_key)],
)
def organization_power_usage_by_location_and_circuit(
    organization_id: str = Path(
        title="Organization ID",
        description="The unique organization ID to query. Format: UUID",
    ),
    start_date_time: str = Query(
        default="",
        description="The timestamp to start the query at. Format example: 2024-04-01T22:00:00Z",
    ),
    end_date_time: str = Query(
        default="",
        description="The timestamp to end the query at. Format example: 2024-04-01T22:28:00Z",
    ),
):
    try:
        # Initialize the DB session
        session = SessionLocal()

        # Gather the org location data
        org_location_data = OrganizationsController.get_organization_locations_by_org_id(
            session=session,
            organization_id=organization_id,
        )

        # Get the sensor data
        location_ids = [old.location_id for old in org_location_data]
        location_sensor_data = CircuitsController.get_sensors_by_location_ids(
            session=session,
            location_ids=location_ids,
        )

        # Loop through each circuit
        results = []
        for d in location_sensor_data:
            # Pass in the appropriate circuit and sensor data for the TS data
            ts_data = query(
                duid=d.sensor_duid,
                circuit=d.circuit_number,
                start=start_date_time,
                end=end_date_time,
            )

            # Sum all the power watts in the returned data set
            total_power_consumed = sum(ts['power_watts'] for ts in ts_data)
            average_power_consumed = round(sum(ts['power_watts'] for ts in ts_data) / len(ts_data), 5)

            results.append(
                CircuitPowerUsageByLocationResponse(
                    location_id=d.location_id,
                    location_name=d.location_name,
                    circuit_data=CircuitPowerUsageResponse(
                        circuit_id=d.circuit_id,
                        circuit_number=d.circuit_number,
                        circuit_name=d.circuit_name,
                        sensor_id=d.sensor_id,
                        sensor_duid=d.sensor_duid,
                        sensor_name=d.sensor_name,
                        wattage_consumed=total_power_consumed,
                        average_wattage_consumed=average_power_consumed,
                    ),
                )
            )

    except Exception as e:
        """
        NOTE: There is much better error handling to do around types of issues.
        ie; DB connection timeout, no data found, invalid parsing of datetimes, ... so on
        for simplicity I'm doing a full catch all for timeboxing to get this done.
        NOTE: Same thing on the status_code=500... I'm taking liberties with simple 500 here
        to allow myself to complete these in a timely maner and show I can handle exceptions.
        """
        raise HTTPException(
            status_code=500,
            detail=f"Server error: {e}"
        )

    return results