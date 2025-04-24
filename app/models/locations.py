import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from . import Base

class Location(Base):
    __tablename__ = 'locations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String(255), nullable=False)
