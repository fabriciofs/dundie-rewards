"""add field currency in person

Revision ID: 9d50a20cb3d0
Revises: 0abdd78b9b2c
Create Date: 2022-09-16 18:46:26.084970

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '9d50a20cb3d0'
down_revision = '0abdd78b9b2c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'person',
        sa.Column(
            'currency',
            sqlmodel.sql.sqltypes.AutoString(),
            nullable=True
        )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'currency')
    # ### end Alembic commands ###
