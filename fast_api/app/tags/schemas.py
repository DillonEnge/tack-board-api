from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagUpdate(TagBase):
    id: int


class TagDelete(BaseModel):
    id: int


class TagOut(TagBase):
    id: int

    class Config:
        orm_mode = True
