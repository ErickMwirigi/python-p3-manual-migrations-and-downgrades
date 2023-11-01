"""Changing column names

Revision ID: d8bf12c36895
Revises: 778418c799be
Create Date: 2023-11-01 14:39:10.265585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8bf12c36895'
down_revision = '778418c799be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='first_name')


def downgrade() -> None:
    op.alter_column('students', 'first_name', new_column_name='name')