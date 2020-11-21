from sqlalchemy import Column, Integer, ForeignKey
from ...db.database import Base


class EventTag(Base):
    __tablename__ = "event_tag"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('event.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))
