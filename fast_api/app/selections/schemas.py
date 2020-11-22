from pydantic import BaseModel


class SelectionBase(BaseModel):
    name: str
    poll_id: int


class SelectionCreate(SelectionBase):
    pass


class SelectionUpdate(SelectionBase):
    id: int


class SelectionDelete(BaseModel):
    id: int


class SelectionOut(SelectionBase):
    id: int

    class Config:
        orm_mode = True
