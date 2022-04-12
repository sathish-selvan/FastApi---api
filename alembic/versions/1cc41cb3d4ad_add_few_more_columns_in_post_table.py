"""add few more columns in post table

Revision ID: 1cc41cb3d4ad
Revises: b80f8539052c
Create Date: 2022-04-12 17:44:27.342915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cc41cb3d4ad'
down_revision = 'b80f8539052c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('published', sa.Boolean(), nullable=False, server_default='true'),
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()"))))
    pass


def downgrade():
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
