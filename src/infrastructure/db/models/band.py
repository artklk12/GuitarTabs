from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.guitarapp.dto import FullBandDTO, MusicianDTO, BandDTO, SongDTO
from .musician import Musician
from src.infrastructure.db.models.base import BaseAlchemyModels


class Band(BaseAlchemyModels):
    __tablename__ = "band_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(125),
        nullable=False,
    )
    songs: Mapped["Song"] = relationship(back_populates="band")
    members: Mapped["Musician"] = relationship(back_populates="bands", secondary='musician_band_table',)

    # Альбомы
    # Дата основания
    # Дата распада

    def to_dto(self) -> BandDTO:
        return BandDTO(
            id=self.id,
            title=self.title,
        )

    def to_full_dto(self,
                    members: list[MusicianDTO] | None = None,
                    songs: list[SongDTO] | None = None
                    ) -> FullBandDTO:
        return FullBandDTO(
            id=self.id,
            title=self.title,
            members=members,
            songs=songs
        )
