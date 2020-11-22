from . import crud
from . import schemas
from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.SelectionOut])
def read_selections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):  # noqa: E501
    selections = crud.get_selections(db, skip=skip, limit=limit)

    return selections


@router.post("/", response_model=schemas.SelectionOut)
def create_selection(selection: schemas.SelectionCreate, db: Session = Depends(get_db)):  # noqa: E501
    selection = crud.create_selection(db, selection)

    return selection


@router.patch("/", response_model=schemas.SelectionOut)
def update_selection(selection: schemas.SelectionUpdate, db: Session = Depends(get_db)):  # noqa: E501
    selection = crud.update_selection(db, selection)

    return selection


@router.delete("/", response_model=schemas.SelectionOut)
def delete_selection(selection: schemas.SelectionDelete, db: Session = Depends(get_db)):  # noqa: E501
    selection = crud.delete_selection(db, selection)

    return selection
