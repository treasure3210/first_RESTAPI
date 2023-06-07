"""empty message

Revision ID: 0919a101c03d
Revises: c396a64be350
Create Date: 2023-06-06 17:51:18.950130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0919a101c03d'
down_revision = 'c396a64be350'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint("email", ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint("email", type_='unique')
        batch_op.drop_column('email')
    # ### end Alembic commands ###
