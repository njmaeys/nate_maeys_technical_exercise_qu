from fastapi import APIRouter

from app.db.session import SessionLocal
from app.db.controllers.circuits import CircuitsController
from services.insights.ts_client import query

router=APIRouter(
    tags=['insights'],
)

@router.get('/circuits/{circuit_id}/power-usage')
def circuits_power_usage_by_id(
    circuit_id: str,
):
    # Initialize the DB session
    session = SessionLocal()

    # Find the circuit and sensor data for the curcuit_id
    circuit_and_sensor_data = CircuitsController.get_circuits_data_by_id(
        session=session,
        circuit_id=circuit_id,
    )
    print("\n### HERE ###")
    print(circuit_and_sensor_data)

    return {'detail':'implement foo'}