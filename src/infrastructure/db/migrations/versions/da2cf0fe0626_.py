"""empty message

Revision ID: da2cf0fe0626
Revises: e81ab9bc4987
Create Date: 2023-07-30 21:29:34.559787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da2cf0fe0626'
down_revision = 'e81ab9bc4987'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('musician_band_table', 'title')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('musician_band_table', sa.Column('title', sa.VARCHAR(length=125), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
