from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.dialects.postgresql import UUID
# import uuid

from ..db.database import Base


# TODO Add sqlite/psql switch for uuid usage
class Tag(Base):
    __tablename__ = "tag"

    # id = Column(UUID(as_uuid=True), default=uuid.uuid4(), primary_key=True, index=True)  # noqa: E501
    id = Column(Integer, primary_key=True, index=True)  # noqa: E501
    name = Column(String, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
