from . import crud
from . import schemas
from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.TagOut])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = crud.get_tags(db, skip=skip, limit=limit)
    return tags


@router.post("/", response_model=schemas.TagOut)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    tag = crud.create_tag(db, tag)
    return tag


@router.patch("/", response_model=schemas.TagOut)
def update_tag(tag: schemas.TagUpdate, db: Session = Depends(get_db)):
    tag = crud.update_tag(db, tag)
    return tag


@router.delete("/", response_model=schemas.TagOut)
def delete_tag(tag: schemas.TagDelete, db: Session = Depends(get_db)):
    tag = crud.delete_tag(db, tag)
    return tag
