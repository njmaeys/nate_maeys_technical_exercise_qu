from pydantic import BaseModel
from uuid import UUID
from typing import Optional

from app.models.circuits import Circuit
from app.models.electric_sensors import ElectricSensor
from app.models.locations import Location


"""
NOTE: 
Normally I'd break these all out into their own controller files but keeping
it in a single one for this project but will break them into classes.
"""


class CircuitQueryModels:
    class CircuitSensorData(BaseModel):
        circuit_id: UUID
        circuit_number: int
        circuit_name: str
        sensor_id: UUID
        sensor_duid: str
        sensor_name: str
        sensor_location_id: UUID
        location_id: Optional[UUID] = None
        location_name: Optional[str] = None

class CircuitsController:
    def get_circuits_data_by_id(session, circuit_id: str) -> CircuitQueryModels.CircuitSensorData:
        # Circuit ID appears to be unique and looks to tie to a single sensior.
        # This means only a single sensor should be returned
        results = (
            session.query(
                Circuit.id.label("circuit_id"),
                Circuit.circuit_number.label("circuit_number"),
                Circuit.name.label("circuit_name"),
                ElectricSensor.id.label("sensor_id"),
                ElectricSensor.duid.label("sensor_duid"),
                ElectricSensor.name.label("sensor_name"),
                ElectricSensor.location_id.label("sensor_location_id"),
            )
            .join(ElectricSensor, Circuit.sensor_id == ElectricSensor.id)
            .filter(Circuit.id == circuit_id)
            .first()
        )

        return CircuitQueryModels.CircuitSensorData(**results._asdict())

    def get_sensors_by_location_ids(session, location_ids: list[str]) -> CircuitQueryModels.CircuitSensorData:
        # Find all the sensors by location ID
        results = (
            session.query(
                ElectricSensor.id.label("sensor_id"),
                ElectricSensor.location_id.label("location_id"),
                ElectricSensor.duid.label("sensor_duid"),
                ElectricSensor.name.label("sensor_name"),
                ElectricSensor.location_id.label("sensor_location_id"),
                Circuit.id.label("circuit_id"),
                Circuit.circuit_number.label("circuit_number"),
                Circuit.name.label("circuit_name"),
                Location.name.label("location_name"),
            )
            .join(Circuit, ElectricSensor.id == Circuit.sensor_id, isouter=True)
            .join(Location, ElectricSensor.location_id == Location.id, isouter=True)
            .filter(ElectricSensor.location_id.in_(location_ids))
            .all()
        )

        return [CircuitQueryModels.CircuitSensorData(**row._asdict()) for row in results]


class OrganizationQueryModels:
    class OrganizationLocationData(BaseModel):
        location_id: UUID
        organization_id: UUID
        name: str


class OrganizationsController:
    def get_organization_locations_by_org_id(session, organization_id: str) -> OrganizationQueryModels.OrganizationLocationData:
        # A given organization may have multiple locations
        results = (
            session.query(
                Location.id.label("location_id"),
                Location.organization_id.label("organization_id"),
                Location.name.label("name"),
            )
            .filter(Location.organization_id == organization_id)
            .all()
        )
        return [OrganizationQueryModels.OrganizationLocationData(**row._asdict()) for row in results]