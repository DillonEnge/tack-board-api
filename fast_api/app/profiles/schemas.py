from pydantic import BaseModel


class ProfileBase(BaseModel):
    name: str
    profile_img: str
    phone_num: str
    description: str


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    id: int


class ProfileDelete(BaseModel):
    id: int


class ProfileOut(ProfileBase):
    id: int

    class Config:
        orm_mode = True
