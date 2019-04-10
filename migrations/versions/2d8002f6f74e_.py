"""empty message

Revision ID: 2d8002f6f74e
Revises: 8f61fb5af9c3
Create Date: 2019-04-10 16:55:08.542473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d8002f6f74e'
down_revision = '8f61fb5af9c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teachers', 'phone')
    op.add_column('users', sa.Column('phone', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone')
    op.add_column('teachers', sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
