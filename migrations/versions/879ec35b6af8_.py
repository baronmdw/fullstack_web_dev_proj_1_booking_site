"""empty message

Revision ID: 879ec35b6af8
Revises: 28a782953c65
Create Date: 2023-02-22 19:03:38.040732

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '879ec35b6af8'
down_revision = '28a782953c65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Show', schema=None) as batch_op:
        batch_op.add_column(sa.Column('detail_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'Showdetail', ['detail_id'], ['id'])
        batch_op.drop_column('start_time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Show', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('detail_id')

    # ### end Alembic commands ###
