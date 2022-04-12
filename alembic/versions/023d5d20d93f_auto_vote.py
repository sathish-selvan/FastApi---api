"""auto-vote

Revision ID: 023d5d20d93f
Revises: 1cc41cb3d4ad
Create Date: 2022-04-12 19:07:38.316507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '023d5d20d93f'
down_revision = '1cc41cb3d4ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
