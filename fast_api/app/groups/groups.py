from . import crud
from . import schemas
from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.GroupOut])
def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):  # noqa: E501
    groups = crud.get_groups(db, skip=skip, limit=limit)
    return groups


@router.post("/", response_model=schemas.GroupOut)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):  # noqa: E501
    group = crud.create_group(db, group)
    return group


@router.patch("/", response_model=schemas.GroupOut)
def update_group(group: schemas.GroupUpdate, db: Session = Depends(get_db)):  # noqa: E501
    group = crud.update_group(db, group)
    return group


@router.delete("/", response_model=schemas.GroupOut)
def delete_group(group: schemas.GroupDelete, db: Session = Depends(get_db)):  # noqa: E501
    group = crud.delete_group(db, group)
    return group
