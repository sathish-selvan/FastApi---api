"""add content column

Revision ID: 49c7eb2eb602
Revises: 448c17169033
Create Date: 2022-04-12 16:08:44.386973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49c7eb2eb602'
down_revision = '448c17169033'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
