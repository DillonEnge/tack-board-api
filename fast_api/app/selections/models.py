from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..db.database import Base


class Selection(Base):
    __tablename__ = "selection"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    poll_id = Column(Integer, ForeignKey('poll.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
