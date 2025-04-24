from pydantic import BaseModel
from uuid import UUID


"""
NOTE:
These response models could def be nested and structured around items like
the location or the circuit but keeping it simple for this exercise.
"""


class CircuitPowerUsageResponse(BaseModel):
    circuit_id: UUID
    circuit_number: int
    circuit_name: str
    sensor_id: UUID
    sensor_duid: str
    sensor_name: str
    wattage_consumed: int
    average_wattage_consumed: float


class CircuitPowerUsageByLocationResponse(BaseModel):
    location_id: UUID
    location_name: str
    circuit_data: CircuitPowerUsageResponse