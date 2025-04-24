from pydantic import BaseModel
from uuid import UUID

from app.models.circuits import Circuit
from app.models.electric_sensors import ElectricSensor


class CircuitQueryModels:
    class CircuitSensorData(BaseModel):
        circuit_id: UUID
        circuit_number: int
        circuit_name: str
        sensor_id: UUID
        sensor_duid: str
        sensor_name: str
        sensor_location_id: UUID

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

