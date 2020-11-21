from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..db.database import Base


# TODO Enforce enums on the db side
class Poll(Base):
    __tablename__ = "poll"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    event_id = Column(Integer, ForeignKey('event.id'))
    poll_type = Column(String, index=True)
    poll_scope = Column(String, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
