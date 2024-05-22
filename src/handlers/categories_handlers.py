from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from keyboards import build_menu_keyboard, build_choose_find_keyboard
from aiogram.fsm.context import FSMContext
from states import find_places


from data import categories, callback_data

router = Router()


@router.callback_query(
    F.data == callback_data['back_from_categories_callback_data'], find_places.category
)
async def back_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.edit_text(text='Меню', reply_markup=build_menu_keyboard())


@router.message(Command('start', 'menu'), find_places.category)
async def start_menu_command_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text='Меню', reply_markup=build_menu_keyboard())


@router.callback_query(F.data.in_(categories.values()), find_places.category)
async def category_handler(callback_query: CallbackQuery, state: FSMContext):
    print(callback_query.data)

    await state.update_data(category=callback_query.data)

    await callback_query.message.edit_text(
        'Выберите поиск', reply_markup=build_choose_find_keyboard()
    )
    await state.set_state(find_places.choose_find)
