from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram import types
from keyboards import build_menu_keyboard
from aiogram.fsm.context import FSMContext
from data import help_text, start_text

router = Router()


@router.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    print(message.from_user.id)
    await message.answer(text=start_text)
    await message.answer(text='Главное меню', reply_markup=build_menu_keyboard())
    await state.clear()


@router.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer(text=help_text)


@router.message(Command('menu'))
async def menu_command(message: types.Message, state: FSMContext):
    await message.answer(text='Главное меню', reply_markup=build_menu_keyboard())
    await state.clear()
