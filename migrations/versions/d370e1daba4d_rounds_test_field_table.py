"""rounds test field table

Revision ID: d370e1daba4d
Revises: 
Create Date: 2021-04-23 11:52:08.188869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd370e1daba4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roundsDB', sa.Column('test_field', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roundsDB', 'test_field')
    # ### end Alembic commands ###
