from . import crud
from . import schemas
from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.ProfileOut])
def read_profiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):  # noqa: E501
    profiles = crud.get_profiles(db, skip=skip, limit=limit)
    return profiles


@router.post("/", response_model=schemas.ProfileOut)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):  # noqa: E501
    profile = crud.create_profile(db, profile)
    return profile


@router.patch("/", response_model=schemas.ProfileOut)
def update_profile(profile: schemas.ProfileUpdate, db: Session = Depends(get_db)):  # noqa: E501
    profile = crud.update_profile(db, profile)
    return profile


@router.delete("/", response_model=schemas.ProfileOut)
def delete_profile(profile: schemas.ProfileDelete, db: Session = Depends(get_db)):  # noqa: E501
    profile = crud.delete_profile(db, profile)
    return profile
