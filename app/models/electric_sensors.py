import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from . import Base


class ElectricSensor(Base):
    __tablename__ = 'electric_sensors'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    duid = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    location_id = Column(UUID(as_uuid=True), ForeignKey('locations.id'), nullable=False)
