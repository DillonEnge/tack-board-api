from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..db.database import Base


# TODO Enforce accessibility enum on the db side
class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    time = Column(String, index=True)
    location = Column(String, index=True)
    description = Column(String, index=True)
    accessibility = Column(String, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    tags = relationship('Tag', secondary='event_tag', backref='Event')
