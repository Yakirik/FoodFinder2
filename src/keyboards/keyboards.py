from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def build_geo_keyboard() -> ReplyKeyboardMarkup:
    geo_button = KeyboardButton(text="Отправить местоположение", request_location=True)
    buttons_row = [geo_button]
    keyboard = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True, keyboard=[buttons_row]
    )

    return keyboard
