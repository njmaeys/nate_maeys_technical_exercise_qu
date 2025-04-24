from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from . import Base


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
