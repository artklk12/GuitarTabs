from src.domain.guitarapp.dto import SongDTO
from src.domain.guitarapp.dto.user import CreateUserDTO, UpdateUserDTO, UserDTO
from src.domain.guitarapp.usecases import CreateUser, GetUserById, GetFavoriteSongsByUser, GetUsers, UpdateUser, \
    DeleteUser
from src.infrastructure.db.uow import UnitOfWork


class UserServices:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def create_user(self, user_dto: CreateUserDTO) -> UserDTO:
        return await CreateUser(self.uow)(user_dto)

    async def get_user_by_id(self, id_: int) -> UserDTO:
        return await GetUserById(self.uow)(id_)

    async def get_favorite_songs_by_user(self, id_: int) -> list[SongDTO]:
        return await GetFavoriteSongsByUser(self.uow)(id_)

    async def get_all_users(self) -> list[UserDTO]:
        return await GetUsers(self.uow)()

    async def update_user(self, update_user_dto: UpdateUserDTO) -> UserDTO:
        await UpdateUser(self.uow)(update_user_dto)
        return await GetUserById(self.uow)(update_user_dto.id)

    async def delete_user(self, id_: int) -> None:
        await DeleteUser(self.uow)(id_)