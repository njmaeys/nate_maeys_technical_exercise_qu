from fastapi import APIRouter, Path, Query, HTTPException

from app.db.session import SessionLocal
from app.db.controllers.circuits import CircuitsController
from services.insights.ts_client import query
from services.insights.responses import CircuitPowerUsageResponse

router=APIRouter(
    tags=['insights'],
)

@router.get(
    '/circuits/{circuit_id}/power-usage',
    description="Returns the total power in watts consumed by a circuit in the requested time period.",
    response_model=CircuitPowerUsageResponse,
)
def circuits_power_usage_by_id(
    circuit_id: str = Path(
        title="Circuit ID",
        description="The unique circuit ID to query. Format: UUID",
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

        # Find the circuit and sensor data for the curcuit_id
        circuit_and_sensor_data = CircuitsController.get_circuits_data_by_id(
            session=session,
            circuit_id=circuit_id,
        )
        
        # Pass in the appropriate circuit and sensor data for the TS data
        ts_data = query(
            duid=circuit_and_sensor_data.sensor_duid,
            circuit=circuit_and_sensor_data.circuit_number,
            start=start_date_time,
            end=end_date_time,
        )

        # Sum all the power watts in the returned data set
        total_power_consumed = sum(ts['power_watts'] for ts in ts_data)
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
    )