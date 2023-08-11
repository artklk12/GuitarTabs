from src.domain.guitarapp.dto import CreateMusicianDTO, MusicianDTO, UpdateMusicianDTO
from src.domain.guitarapp.exceptions import MusicianNotExists
from src.domain.guitarapp.usecases import MusicianUseCase
from src.infrastructure.db.uow import UnitOfWork


class GetMusicianById(MusicianUseCase):
    async def __call__(self, id_: int) -> MusicianDTO:
        if musician := await self.uow.app_holder.musician_repo.get_by_id(id_):
            return musician
        raise MusicianNotExists


class CreateMusician(MusicianUseCase):
    async def __call__(self, musician_dto: CreateMusicianDTO) -> MusicianDTO:
        return await self.uow.app_holder.musician_repo.create_obj(musician_dto)


class GetMusicians(MusicianUseCase):
    async def __call__(self) -> list[MusicianDTO]:
        return await self.uow.app_holder.musician_repo.get_all()


class UpdateMusician(MusicianUseCase):
    async def __call__(self, musician_update_dto: UpdateMusicianDTO) -> None:
        if await self.uow.app_holder.musician_repo.get_by_id(musician_update_dto.id):
            await self.uow.app_holder.musician_repo.update_obj(
                musician_update_dto.id,
                **musician_update_dto.dict(exclude_none=True, exclude=set("id")),
            )
            return
        else:
            raise MusicianNotExists


class DeleteMusician(MusicianUseCase):
    async def __call__(self, id_: int) -> None:
        if await self.uow.app_holder.musician_repo.get_by_id(id_):
            await self.uow.app_holder.musician_repo.delete_obj(id_)
            return
        raise MusicianNotExists


class MusicianServices:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def create_musician(self, musician_dto: CreateMusicianDTO) -> MusicianDTO:
        async with self.uow:
            musician = await CreateMusician(self.uow)(musician_dto)
            await self.uow.commit()
            return musician

    async def get_all_musicians(self) -> list[MusicianDTO]:
        return await GetMusicians(self.uow)()

    async def get_musician_by_id(self, id_: int) -> MusicianDTO:
        return await GetMusicianById(self.uow)(id_)

    async def update_musician(self, update_musician_dto: UpdateMusicianDTO) -> MusicianDTO:
        async with self.uow:
            await UpdateMusician(self.uow)(update_musician_dto)
            await self.uow.commit()
            return await GetMusicianById(self.uow)(update_musician_dto.id)

    async def delete_musician(self, id_: int) -> None:
        async with self.uow:
            await DeleteMusician(self.uow)(id_)
            await self.uow.commit()
