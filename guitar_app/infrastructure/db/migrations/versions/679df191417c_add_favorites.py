"""add favorites

Revision ID: 679df191417c
Revises: 7350b0efd751
Create Date: 2023-08-13 17:38:18.178857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '679df191417c'
down_revision = '7350b0efd751'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_favorite_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['song_table.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user_table.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'song_id', name='user_favorite_song_ff')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_favorite_table')
    # ### end Alembic commands ###