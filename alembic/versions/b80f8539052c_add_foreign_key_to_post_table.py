"""add foreign_key_to_post_table

Revision ID: b80f8539052c
Revises: 56ad97adcd62
Create Date: 2022-04-12 17:04:11.543354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b80f8539052c'
down_revision = '56ad97adcd62'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column("owner_id", sa.Integer(), nullable=False ))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts','owner_id')
    pass
