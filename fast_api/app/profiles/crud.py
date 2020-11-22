from sqlalchemy.orm import Session

from datetime import datetime, timezone

from . import models
from . import schemas


def get_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profile).filter(models.Profile.deleted_at == None).offset(skip).limit(limit).all()  # noqa: E501, E711


def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(**profile.dict())
    db_profile.created_at = datetime.now(timezone.utc)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    return db_profile


def update_profile(db: Session, profile: schemas.ProfileUpdate):
    db_profile = db.query(models.Profile).get(profile.id)
    db_profile.name = profile.name
    db_profile.profile_img = profile.profile_img
    db_profile.phone_num = profile.phone_num
    db_profile.description = profile.description
    db_profile.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_profile)

    return db_profile


def delete_profile(db: Session, profile: schemas.ProfileDelete):
    db_profile = db.query(models.Profile).get(profile.id)
    db_profile.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_profile)

    return db_profile
