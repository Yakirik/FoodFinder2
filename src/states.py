from aiogram.fsm.state import StatesGroup, State


class find_places(StatesGroup):
    category = State()
    choose_find = State()
    metro = State()
    geo = State()
    choose_place = State()
