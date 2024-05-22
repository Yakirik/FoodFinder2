from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards import build_categories_keyboard
from aiogram.fsm.context import FSMContext
from states import find_places
from data import callback_data, help_text

router = Router()


@router.callback_query(F.data == callback_data['categories_callback_data'])
async def categories_menu_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(find_places.category)
    await callback_query.message.edit_text(
        text='Категории', reply_markup=build_categories_keyboard()
    )


@router.callback_query(F.data == callback_data['favorites_callback_data'])
async def favorites_menu_handler(callback_query: CallbackQuery):
    await callback_query.answer(text='Покамись пусто')


@router.callback_query(F.data == callback_data['help_callback_data'])
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text=help_text)
