from pydantic import BaseModel
from uuid import UUID

# NOTE: This could be nested into objects of circuit and sensor.
# Keeping top level for end user ease of access since this is a small endpoint.
class CircuitPowerUsageResponse(BaseModel):
    circuit_id: UUID
    circuit_number: int
    circuit_name: str
    sensor_id: UUID
    sensor_duid: str
    sensor_name: str
    wattage_consumed: int