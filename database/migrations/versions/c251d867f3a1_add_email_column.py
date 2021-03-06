"""Add email column

Revision ID: c251d867f3a1
Revises: b3a639206da1
Create Date: 2022-01-09 22:08:21.934365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c251d867f3a1'
down_revision = 'b3a639206da1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('email', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'email')
    # ### end Alembic commands ###
