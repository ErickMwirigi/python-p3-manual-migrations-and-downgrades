"""Renaming students to scholars

Revision ID: 778418c799be
Revises: 791279dd0760
Create Date: 2023-11-01 14:25:27.324891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '778418c799be'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    

def downgrade() -> None:
    op.rename_table('scholars', 'students')
    