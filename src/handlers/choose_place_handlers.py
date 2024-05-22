from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import build_categories_keyboard, build_place_info

from aiogram.fsm.context import FSMContext
from states import find_places
from data import callback_data

router = Router()


def get_title(place_info: dict) -> str:
    return '{0}\n⭐️Рейтинг заведения: {1}\n📍Адрес: {2}'.format(
        place_info['name'], place_info['reviews']['general_rating'], place_info['address_name']
    )


@router.callback_query(
    F.data == callback_data['back_from_choose_place_data'], find_places.choose_place
)
async def back_from_choose_place_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(find_places.category)
    await state.set_data({})
    await callback_query.message.edit_text(
        text='Категории', reply_markup=build_categories_keyboard()
    )


@router.callback_query(find_places.choose_place)
async def choose_place_handler(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    places_data = user_data['places']
    for place in places_data:
        if place['id'] == callback_query.data:
            await callback_query.message.answer(
                text=get_title(place),
                reply_markup=build_place_info(callback_query.data, user_data, place['point']),
            )
            break


@router.callback_query(
    F.data == callback_data['back_from_choose_place_data'], find_places.choose_place
)
async def back_choose_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(find_places.category)
    await callback_query.message.edit_text(text='Меню', reply_markup=build_categories_keyboard())
