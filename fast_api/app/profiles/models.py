from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.dialects.postgresql import UUID
# import uuid

from ..db.database import Base


# TODO Add sqlite/psql switch for uuid usage
class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)  # noqa: E501
    name = Column(String, index=True)
    profile_img = Column(String, index=True)
    phone_num = Column(String, index=True)
    description = Column(String, index=True)
    # user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
