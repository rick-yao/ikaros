"""Update refresh url

Revision ID: a9c9e7063598
Revises: ef9c9dbb8a8e
Create Date: 2021-08-21 13:36:32.737312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9c9e7063598'
down_revision = 'ef9c9dbb8a8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('refresh_url', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.drop_column('refresh_url')

    # ### end Alembic commands ###
