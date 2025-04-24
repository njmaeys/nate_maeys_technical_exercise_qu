import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from . import Base


class Organization(Base):
    __tablename__ = 'organizations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    brand_id = Column(UUID(as_uuid=True), ForeignKey('brands.id'), nullable=False)
    name = Column(String(255), nullable=False)
