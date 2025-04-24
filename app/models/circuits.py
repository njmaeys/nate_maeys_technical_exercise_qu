import uuid
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from . import Base


class Circuit(Base):
    __tablename__ = 'circuits'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sensor_id = Column(UUID(as_uuid=True), ForeignKey('electric_sensors.id'), nullable=False)
    name = Column(String(255), nullable=False)
    circuit_number = Column(Integer, nullable=False)