from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from guitar_app.application.guitar import dto, services
from guitar_app.application.guitar.domain.services.modulation import get_modulated_verses
from guitar_app.application.guitar.dto import GetSongDTO
from guitar_app.application.guitar.exceptions import SongNotExists
from guitar_app.infrastructure.db.uow import UnitOfWork
from guitar_app.presentation.tgbot import states


async def refresh_mod_value(c: CallbackQuery, widget: Any, manager: DialogManager):
    await c.answer()
    data = manager.dialog_data
    data['mod_value'] = 0
    print('Изменение тональности сброшено')


async def up_key(c: CallbackQuery, widget: Any, manager: DialogManager):
    await c.answer()
    data = manager.dialog_data
    if data['mod_value'] < 11:
        data['mod_value'] += 1
    else:
        data['mod_value'] = 0
    print('Изменить тональность на', data['mod_value'])
    await manager.switch_to(states.FavoriteSongsPanelSG.modulated_chords)


async def up_key_with_tabs(c: CallbackQuery, widget: Any, manager: DialogManager):
    await c.answer()
    data = manager.dialog_data
    if data['mod_value'] < 11:
        data['mod_value'] += 1
    else:
        data['mod_value'] = 0
    print('Изменить тональность на', data['mod_value'])
    await manager.switch_to(states.FavoriteSongsPanelSG.modulated_song_chords_with_tabs)


async def down_key(c: CallbackQuery, widget: Any, manager: DialogManager):
    await c.answer()
    data = manager.dialog_data
    if data['mod_value'] > -11:
        data['mod_value'] -= 1
    else:
        data['mod_value'] = 0
    print('Изменить тональность на', data['mod_value'])
    await manager.switch_to(states.FavoriteSongsPanelSG.modulated_chords)


async def down_key_with_tabs(c: CallbackQuery, widget: Any, manager: DialogManager):
    await c.answer()
    data = manager.dialog_data
    if data['mod_value'] > -11:
        data['mod_value'] -= 1
    else:
        data['mod_value'] = 0
    print('Изменить тональность на', data['mod_value'])
    await manager.switch_to(states.FavoriteSongsPanelSG.modulated_song_chords_with_tabs)


async def select_song(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    await c.answer()
    data = manager.dialog_data
    if not isinstance(data, dict):
        data = {}
    data["song_id"] = int(item_id)
    await manager.switch_to(states.AllSongsPanelSG.song_menu)


async def select_song_founded_by_title(
    c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str
):
    await c.answer()
    data = manager.dialog_data
    if not isinstance(data, dict):
        data = {}
    data["song_id"] = int(item_id)
    await manager.switch_to(states.FoundedSongsPanelSG.song_menu)


async def select_song_by_band(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    await c.answer()
    data = manager.dialog_data
    if not isinstance(data, dict):
        data = {}
    data["song_id"] = int(item_id)
    await manager.switch_to(states.BandSongsPanelSG.song_menu)


async def select_favorite_song(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    await c.answer()
    data = manager.dialog_data
    if not isinstance(data, dict):
        data = {}
    data["song_id"] = int(item_id)
    data['mod_value'] = 0
    await manager.switch_to(states.FavoriteSongsPanelSG.song_menu)


async def add_song_to_favorite(c: CallbackQuery, widget: Button, manager: DialogManager):
    await c.answer()
    song_id = manager.dialog_data["song_id"]
    user: dto.UserDTO = manager.middleware_data["user"]
    uow: UnitOfWork = manager.middleware_data["uow"]
    try:
        await services.SongServices(uow).add_song_to_favorite(
            dto.FavoriteSongDTO(song_id=song_id, user_id=user.telegram_id)
        )
    except SongNotExists:
        return


async def remove_song_from_favorite(c: CallbackQuery, widget: Button, manager: DialogManager):
    await c.answer()
    song_id = manager.dialog_data["song_id"]
    user: dto.UserDTO = manager.middleware_data["user"]
    uow: UnitOfWork = manager.middleware_data["uow"]
    try:
        return await services.SongServices(uow).remove_song_from_favorite(
            dto.FavoriteSongDTO(song_id=song_id, user_id=user.telegram_id)
        )
    except SongNotExists:
        return


async def find_song_by_title(m: Message, dialog: Any, manager: DialogManager):
    if not m.text:
        await manager.switch_to(states.FoundedSongsPanelSG.message_type_error)
    else:
        data = manager.dialog_data
        if not isinstance(data, dict):
            data = {}
        data["song_title"] = m.text.strip()
        await manager.switch_to(states.FoundedSongsPanelSG.choose_song)
