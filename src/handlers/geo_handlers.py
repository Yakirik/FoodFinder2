from aiogram import Router, F
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram import types
from keyboards import build_menu_keyboard, build_choose_place
from aiogram.fsm.context import FSMContext
from states import find_places

from data import callback_data
from requests import get_places_geo

router = Router()


def get_title(places: list) -> str:
    res = ''
    for i, place in enumerate(places):
        res += '{0}. {1}\n\n'.format(i + 1, place['name'])
    return res


@router.callback_query(F.data == callback_data['back_from_geo_callback_data'], find_places.geo)
async def geo_back_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.edit_text('Меню', reply_markup=build_menu_keyboard())
    await callback_query.answer(text='Отмена поиска')
    await state.clear()


@router.message(Command('start', 'menu'), find_places.geo)
async def start_menu_command_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text='Меню', reply_markup=build_menu_keyboard())


@router.message(find_places.geo)
async def location_handler(message: types.Message, state: FSMContext):

    if message.location is not None:
        await state.update_data(
            user_loc={
                'lon': str(message.location.longitude),
                'lat': str(message.location.latitude),
            }
        )
        user_data = await state.get_data()
        places = await get_places_geo(user_data)

        await message.answer(text='Выберите заведение', reply_markup=ReplyKeyboardRemove())
        await message.answer(text=get_title(places), reply_markup=build_choose_place(places))
        await state.update_data(places=places)
        await state.set_state(find_places.choose_place)
    else:
        pass
