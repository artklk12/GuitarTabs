"""empty message

Revision ID: 13f744c06e86
Revises:
Create Date: 2023-09-05 12:02:30.904253

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "13f744c06e86"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "band_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=125), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "musician_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=125), nullable=False),
        sa.Column("last_name", sa.String(length=125), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("telegram_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id"),
    )
    op.create_table(
        "musician_band_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("band_id", sa.Integer(), nullable=False),
        sa.Column("musician_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["band_id"], ["band_table.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["musician_id"], ["musician_table.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("band_id", "musician_id", name="musician_band_ff"),
    )
    op.create_table(
        "song_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=125), nullable=False),
        sa.Column("band_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["band_id"], ["band_table.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_favorite_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("song_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["song_id"], ["song_table.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["user_table.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "song_id", name="user_favorite_song_ff"),
    )
    op.create_table(
        "verse_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=125), nullable=False),
        sa.Column("song_id", sa.Integer(), nullable=False),
        sa.Column("lyrics", sa.String(length=500), nullable=True),
        sa.Column("chords", sa.String(length=250), nullable=True),
        sa.ForeignKeyConstraint(["song_id"], ["song_table.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("verse_table")
    op.drop_table("user_favorite_table")
    op.drop_table("song_table")
    op.drop_table("musician_band_table")
    op.drop_table("user_table")
    op.drop_table("musician_table")
    op.drop_table("band_table")
    # ### end Alembic commands ###