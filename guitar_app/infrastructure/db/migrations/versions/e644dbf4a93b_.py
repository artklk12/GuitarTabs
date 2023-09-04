"""empty message

Revision ID: e644dbf4a93b
Revises: ccc5c802dddd
Create Date: 2023-07-30 21:14:33.169708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e644dbf4a93b'
down_revision = 'ccc5c802dddd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('band_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=125), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('musician_band_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('band_id', sa.Integer(), nullable=False),
    sa.Column('musician_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=125), nullable=False),
    sa.ForeignKeyConstraint(['band_id'], ['band_table.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['musician_id'], ['musician_table.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('song_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('band_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=125), nullable=False),
    sa.Column('lyrics', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['band_id'], ['band_table.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song_table')
    op.drop_table('musician_band_table')
    op.drop_table('band_table')
    # ### end Alembic commands ###