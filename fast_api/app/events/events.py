from . import crud
from . import schemas
from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.EventOut])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):  # noqa: E501
    events = crud.get_events(db, skip=skip, limit=limit)

    return events


@router.post("/", response_model=schemas.EventOut)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    event = crud.create_event(db, event)

    return event


@router.patch("/", response_model=schemas.EventOut)
def update_event(event: schemas.EventUpdate, db: Session = Depends(get_db)):
    event = crud.update_event(db, event)

    return event


@router.delete("/", response_model=schemas.EventOut)
def delete_event(event: schemas.EventDelete, db: Session = Depends(get_db)):
    event = crud.delete_event(db, event)

    return event
