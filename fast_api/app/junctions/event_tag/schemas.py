from pydantic import BaseModel


class EventTagBase(BaseModel):
    event_id: int
    tag_id: int
