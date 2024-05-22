from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram import types
from keyboards import (
    build_menu_keyboard,
    build_choose_station_keyboard,
    build_geo_back_keyboard,
    build_categories_keyboard,
)
from keyboards import build_geo_keyboard
from aiogram.fsm.context import FSMContext
from states import find_places

from data import callback_data, geo_help_text

router = Router()


@router.message(Command('start', 'menu'), find_places.choose_find)
async def start_command_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text='Отмена поиска')
    await message.answer(text='Меню', reply_markup=build_menu_keyboard())


@router.callback_query(
    F.data == callback_data['metro_search_callback_data'], find_places.choose_find
)
async def choose_metro_handler(callback_query: CallbackQuery, state: FSMContext):

    await callback_query.message.edit_text(
        text='Выберите станцию метро', reply_markup=build_choose_station_keyboard()
    )
    await state.set_state(find_places.metro)


@router.callback_query(
    F.data == callback_data['geo_search_callback_data'], find_places.choose_find
)
async def choose_geo_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(find_places.geo)
    await callback_query.message.edit_text(
        text='Отправьте геопозицию', reply_markup=build_geo_back_keyboard()
    )
    await callback_query.message.answer(text=geo_help_text, reply_markup=build_geo_keyboard())


@router.callback_query(
    F.data == callback_data['back_from_choose_find_callback_data'], find_places.choose_find
)
async def back_choose_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(find_places.category)
    await callback_query.message.edit_text(text='Меню', reply_markup=build_categories_keyboard())
