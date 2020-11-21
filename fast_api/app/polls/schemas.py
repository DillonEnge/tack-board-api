from pydantic import BaseModel, Field
from enum import Enum
from ..events import schemas as e_schemas


class TypeEnum(str, Enum):
    checklist = 'checklist'
    description = 'description'


class ScopeEnum(str, Enum):
    moderator_only = 'moderator_only'
    all_members = 'all_members'


class PollBase(BaseModel):
    question: str


class PollCreate(PollBase):
    event_id: int
    poll_type: TypeEnum = Field(alias='poll_type')
    poll_scope: ScopeEnum = Field(alias='scope_type')


class PollUpdate(PollBase):
    id: int
    poll_type: TypeEnum = Field(alias='poll_type')
    poll_scope: ScopeEnum = Field(alias='scope_type')


class PollDelete(BaseModel):
    id: int


class PollOut(PollBase):
    id: int
    event: e_schemas.EventOut
    poll_type: str
    poll_scope: str

    class Config:
        orm_mode = True
