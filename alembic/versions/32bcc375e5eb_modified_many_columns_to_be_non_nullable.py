"""Modified many columns to be non-nullable

Revision ID: 32bcc375e5eb
Revises: 1c2565344194
Create Date: 2020-06-22 01:02:21.959836

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '32bcc375e5eb'
down_revision = '1c2565344194'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event', 'description',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('event', 'location',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('event', 'time',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('event_group', 'event_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('event_group', 'group_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('event_tag', 'event_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('event_tag', 'tag_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('poll', 'event_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('poll', 'scope',
               existing_type=postgresql.ENUM('moderator_only', 'all_members', name='poll_scope'),
               nullable=False)
    op.alter_column('poll', 'type',
               existing_type=postgresql.ENUM('checklist', 'description', name='poll_type'),
               nullable=False)
    op.alter_column('profile', 'description',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('profile', 'phone_number',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('profile', 'profile_img',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('profile', 'user_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('profile_event_role', 'event_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('profile_event_role', 'profile_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('profile_event_role', 'role',
               existing_type=postgresql.ENUM('leader', 'admin', 'member', name='role_type'),
               nullable=False)
    op.alter_column('profile_group_role', 'group_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('profile_group_role', 'profile_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('profile_group_role', 'role',
               existing_type=postgresql.ENUM('leader', 'admin', 'member', name='role_type'),
               nullable=False)
    op.alter_column('profile_selection', 'profile_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('profile_selection', 'selection_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('selection', 'poll_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('selection', 'poll_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('profile_selection', 'selection_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('profile_selection', 'profile_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('profile_group_role', 'role',
               existing_type=postgresql.ENUM('leader', 'admin', 'member', name='role_type'),
               nullable=True)
    op.alter_column('profile_group_role', 'profile_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('profile_group_role', 'group_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('profile_event_role', 'role',
               existing_type=postgresql.ENUM('leader', 'admin', 'member', name='role_type'),
               nullable=True)
    op.alter_column('profile_event_role', 'profile_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('profile_event_role', 'event_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('profile', 'user_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('profile', 'profile_img',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('profile', 'phone_number',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('profile', 'description',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('poll', 'type',
               existing_type=postgresql.ENUM('checklist', 'description', name='poll_type'),
               nullable=True)
    op.alter_column('poll', 'scope',
               existing_type=postgresql.ENUM('moderator_only', 'all_members', name='poll_scope'),
               nullable=True)
    op.alter_column('poll', 'event_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('event_tag', 'tag_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('event_tag', 'event_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('event_group', 'group_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('event_group', 'event_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('event', 'time',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('event', 'location',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('event', 'description',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###