from pydantic import BaseModel, Field
from enum import Enum


class AccessibilityEnum(str, Enum):
    public = 'public'
    private = 'private'


class GroupBase(BaseModel):
    name: str
    group_img: str
    description: str


class GroupCreate(GroupBase):
    accessibility: AccessibilityEnum = Field(alias='accessibility')


class GroupUpdate(GroupBase):
    id: int
    accessibility: AccessibilityEnum = Field(alias='accessibility')


class GroupDelete(BaseModel):
    id: int


class GroupOut(GroupBase):
    id: int
    accessibility: str

    class Config:
        orm_mode = True
