"""empty message

Revision ID: 8a5f585a29fe
Revises: f3d406349071
Create Date: 2021-04-23 11:58:46.192751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a5f585a29fe'
down_revision = 'f3d406349071'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roundsDB') as batch_op:
        batch_op.drop_column('test_field')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roundsDB', sa.Column('test_field', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
