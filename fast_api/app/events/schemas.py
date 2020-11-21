from datetime import datetime
from pydantic import BaseModel, Field
from typing import List
from enum import Enum
from ..tags import schemas as t_schemas


class AccessibilityEnum(str, Enum):
    public = 'public'
    private = 'private'


class EventBase(BaseModel):
    name: str
    description: str
    time: datetime
    location: str


class EventCreate(EventBase):
    tags: List[int]
    accessibility: AccessibilityEnum = Field(alias='accessibility')


class EventUpdate(EventBase):
    id: int
    tags: List[int]
    accessibility: AccessibilityEnum = Field(alias='accessibility')


class EventDelete(BaseModel):
    id: int


class EventOut(EventBase):
    id: int
    tags: List[t_schemas.TagOut]
    accessibility: str

    class Config:
        orm_mode = True
