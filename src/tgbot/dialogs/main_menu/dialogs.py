from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Jinja, Const

from src.tgbot import states
from src.tgbot.dialogs.main_menu.getters import get_main

main_menu = Dialog(
    Window(
        Jinja(
            "Привет, {{ username }}!\n"
            "Ты находишься в главном меню.\n"
        ),
        # Start(
        #     Const("[Emodji]История поиска"),
        #     id="search_history",
        #     state=states.SearchHistoryPanelSG.list,
        # ),
        Start(
            Const("[Emodji]Все песни"),
            id="all_songs",
            state=states.AllSongsPanelSG.choose_song,
        ),
        Start(
            Const("[Emodji]Все группы"),
            id="all_bands",
            state=states.AllBandsPanelSG.choose_band,
        ),
        Start(
            Const("[Emodji]Избранные песни"),
            id="favorite_songs",
            state=states.FavoriteSongsPanelSG.list,
        ),
        # Надо еще добавить поиск песен
        Cancel(Const("[Emodji]Закрыть")),
        state=states.MainMenuSG.main,
        getter=get_main,
    ),
)