"""create user table

Revision ID: 56ad97adcd62
Revises: 49c7eb2eb602
Create Date: 2022-04-12 16:31:29.848712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56ad97adcd62'
down_revision = '49c7eb2eb602'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                sa.Column('id', sa.Integer(), nullable=False),
                sa.Column('email',sa.String(), nullable=False),
                sa.Column('password', sa.String(), nullable=False),
                sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                sa.PrimaryKeyConstraint('id'),
                sa.UniqueConstraint('email')
                )
    pass


def downgrade():
    op.drop_table('users')
    pass
