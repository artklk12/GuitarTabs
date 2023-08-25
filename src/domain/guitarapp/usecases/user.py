from src.domain.common.usecases.base import BaseUseCase
from src.domain.guitarapp.dto import CreateUserDTO, UserDTO, SongDTO, UpdateUserDTO
from src.infrastructure.db.uow import UnitOfWork
from src.domain.guitarapp.exceptions import UserNotExists


class UserUseCase(BaseUseCase):
    def __init__(self, uow: UnitOfWork) -> None:
        super().__init__(uow)


class CreateUser(UserUseCase):
    async def __call__(self, user_dto: CreateUserDTO) -> UserDTO:
        user = await self.uow.app_holder.user_repo.create_user(user_dto)
        await self.uow.commit()
        return user


class GetUserById(UserUseCase):
    async def __call__(self, id_: int) -> UserDTO:
        user = await self.uow.app_holder.user_repo.get_user_by_id(id_)
        return user


class GetFavoriteSongsByUser(UserUseCase):
    async def __call__(self, id_: int) -> list[SongDTO]:
        return await self.uow.app_holder.favorites_repo.get_all(id_)


class GetUsers(UserUseCase):
    async def __call__(self) -> list[UserDTO]:
        return await self.uow.app_holder.user_repo.get_all_users()


class UpdateUser(UserUseCase):
    async def __call__(self, user_update_dto: UpdateUserDTO) -> None:
        await self.uow.app_holder.user_repo.update_user(
            user_update_dto.id,
            **user_update_dto.dict(exclude_none=True, exclude=set("id"))
        )
        await self.uow.commit()


class DeleteUser(UserUseCase):
    async def __call__(self, id_: int) -> None:
        if await self.uow.app_holder.user_repo.get_user_by_id(id_):
            await self.uow.app_holder.user_repo.delete_user(id_)
            await self.uow.commit()
            return
        raise UserNotExists

