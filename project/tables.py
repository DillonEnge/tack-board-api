import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, Enum
import enum
from sqlalchemy.dialects.postgresql import UUID
from project.settings import Settings
from environs import Env
import uuid

metadata = sqlalchemy.MetaData()
env = Env()
env.read_env()
engine = create_engine(Settings.DB_URL)
metadata.bind = engine

type_enum = ("checklist", "description")
scope_enum = ("moderator_only", "all_members")

class TypeEnum(enum.Enum):
    checklist = 0
    description = 1

class ScopeEnum(enum.Enum):
    moderator_only = 0
    all_members = 1

class RollTypeEnum(enum.Enum):
    leader = 0
    admin = 1
    member = 2

event = sqlalchemy.Table(
    'event',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('description', sqlalchemy.String(length=100)),
    sqlalchemy.Column('time', sqlalchemy.String(length=100)),
    sqlalchemy.Column('location', sqlalchemy.String(length=100)),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

tag = sqlalchemy.Table(
    'tag',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False, unique=True),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

event_tag = sqlalchemy.Table(
    'event_tag',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('event_id', UUID(as_uuid=True), ForeignKey('event.id')),
    sqlalchemy.Column('tag_id', UUID(as_uuid=True), ForeignKey('tag.id'))
)

group = sqlalchemy.Table(
    'group',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('description', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('group_img', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

poll = sqlalchemy.Table(
    'poll',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('question', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('event_id', UUID(as_uuid=True), ForeignKey('event.id')),
    sqlalchemy.Column('type', Enum(TypeEnum, name="poll_type")),
    sqlalchemy.Column('scope', Enum(ScopeEnum, name="poll_scope")),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

profile = sqlalchemy.Table(
    'profile',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('profile_img', sqlalchemy.String(length=100)),
    sqlalchemy.Column('phone_number', sqlalchemy.String(length=100)),
    sqlalchemy.Column('description', sqlalchemy.String(length=100)),
    sqlalchemy.Column('user_id', UUID(as_uuid=True), ForeignKey('user.id')),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

user = sqlalchemy.Table(
    'user',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('username', sqlalchemy.String(length=100), nullable=False, unique=True),
    sqlalchemy.Column('password', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('email', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

refresh_token = sqlalchemy.Table(
    'refresh_token',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False, unique=True),
    sqlalchemy.Column('token', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

profile_group_role = sqlalchemy.Table(
    'profile_group_role',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('profile_id', UUID(as_uuid=True), ForeignKey('profile.id')),
    sqlalchemy.Column('group_id', UUID(as_uuid=True), ForeignKey('group.id')),
    sqlalchemy.Column('role', Enum(RollTypeEnum, name="role_type")),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

profile_event_role = sqlalchemy.Table(
    'profile_event_role',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('profile_id', UUID(as_uuid=True), ForeignKey('profile.id')),
    sqlalchemy.Column('event_id', UUID(as_uuid=True), ForeignKey('event.id')),
    sqlalchemy.Column('role', Enum(RollTypeEnum, name="role_type")),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

event_group = sqlalchemy.Table(
    'event_group',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('event_id', UUID(as_uuid=True), ForeignKey('event.id')),
    sqlalchemy.Column('group_id', UUID(as_uuid=True), ForeignKey('group.id')),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)
selection = sqlalchemy.Table(
    'selection',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column('poll_id', UUID(as_uuid=True), ForeignKey('poll.id')),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

profile_selection = sqlalchemy.Table(
    'profile_selection',
    metadata,
    sqlalchemy.Column('id', UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column('profile_id', UUID(as_uuid=True), ForeignKey('profile.id')),
    sqlalchemy.Column('selection_id', UUID(as_uuid=True), ForeignKey('selection.id')),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column('deleted_at', sqlalchemy.DateTime, nullable=True)
)

def setup_tables():
    metadata.create_all()

def get_metadata():
    return metadata

def get_type_enum():
    return TypeEnum

def get_scope_enum():
    return ScopeEnum

def get_roll_type_enum():
    return RollTypeEnum
