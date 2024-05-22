from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from keyboards import (
    build_menu_keyboard,
    build_choose_place,
    build_choose_find_keyboard,
)
from aiogram.fsm.context import FSMContext
from states import find_places
from requests import get_places_metro


from data import callback_data, stations, stations_loc

router = Router()


def get_title(places: list) -> str:
    res = ''
    for i, place in enumerate(places):
        res += '{0}. {1}\n\n'.format(i + 1, place['name'])
    return res


@router.callback_query(F.data == callback_data['back_from_metro_callback_data'], find_places.metro)
async def back_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(find_places.choose_find)
    await callback_query.message.edit_text(text='Меню', reply_markup=build_choose_find_keyboard())


@router.message(Command('start', 'menu'), find_places.metro)
async def start_command_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text='отмена поиска')
    await message.answer(text='Меню', reply_markup=build_menu_keyboard())


@router.callback_query(F.data.in_(stations.values()), find_places.metro)
async def metro_handler(callback_query: CallbackQuery, state: FSMContext):

    await state.update_data(metro=callback_query.data, user_loc=stations_loc[callback_query.data])
    user_data = await state.get_data()
    places = await get_places_metro(user_data)
    print(f'user_data: {user_data}')
    await callback_query.message.edit_text(
        text=get_title(places), reply_markup=build_choose_place(places)
    )
    await state.update_data(places=places)
    await state.set_state(find_places.choose_place)
