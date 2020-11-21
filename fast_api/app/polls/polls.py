from . import crud
from . import schemas
from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.PollOut])
def read_polls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):  # noqa: E501
    polls = crud.get_polls(db, skip=skip, limit=limit)

    return polls


@router.post("/", response_model=schemas.PollOut)
def create_poll(poll: schemas.PollCreate, db: Session = Depends(get_db)):
    poll = crud.create_poll(db, poll)

    return poll


@router.patch("/", response_model=schemas.PollOut)
def update_poll(poll: schemas.PollUpdate, db: Session = Depends(get_db)):
    poll = crud.update_poll(db, poll)

    return poll


@router.delete("/", response_model=schemas.PollOut)
def delete_poll(poll: schemas.PollDelete, db: Session = Depends(get_db)):
    poll = crud.delete_poll(db, poll)

    return poll
