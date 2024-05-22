from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data import callback_data, stations, categories


def build_menu_keyboard() -> InlineKeyboardMarkup:

    builder = InlineKeyboardBuilder()
    builder.button(text='🍽Категории', callback_data=callback_data['categories_callback_data'])
    builder.button(text='❓Помощь', callback_data=callback_data['help_callback_data'])
    return builder.as_markup()


def build_categories_keyboard() -> InlineKeyboardMarkup:

    builder = InlineKeyboardBuilder()
    builder.button(text='🍣Суши', callback_data=categories['sushi_callback_data'])
    builder.button(text='🍕Пицца', callback_data=categories['pizza_callback_data'])
    builder.button(text='🍜Паназиатская кухня', callback_data=categories['asian_callback_data'])
    builder.button(text='🍽Рестораны', callback_data=categories['restuarants_callback_data'])
    builder.button(text='🥣Кафе', callback_data=categories['cafes_callback_data'])
    builder.button(text='☕️Кофе', callback_data=categories['coffee_callback_data'])
    builder.button(text='🍔Бургеры', callback_data=categories['burgers_callback_data'])
    builder.button(text='🍺Бары', callback_data=categories['bars_callback_data'])
    builder.button(text='🌯Шаурма', callback_data=categories['streetfood_callback_data'])
    builder.button(
        text='⬇️Назад', callback_data=callback_data['back_from_categories_callback_data']
    )

    builder.adjust(2)

    return builder.as_markup()


def build_geo_back_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Назад', callback_data=callback_data['back_from_geo_callback_data'])
    return builder.as_markup()


def build_choose_find_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Ⓜ️Поиск по станции метро', callback_data=callback_data['metro_search_callback_data']
    )
    builder.button(
        text='📍Поиск по геопозиции', callback_data=callback_data['geo_search_callback_data']
    )
    builder.button(
        text='⬇️Назад', callback_data=callback_data['back_from_choose_find_callback_data']
    )
    builder.adjust(1)
    return builder.as_markup()


def build_choose_station_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text='🔴Красный проспект', callback_data=stations['red_av'])
    builder.button(text='🔴Площадь Ленина  ', callback_data=stations['lenina'])
    builder.button(text='🔴Площадь Маркса  ', callback_data=stations['marksa'])
    builder.button(text='🔴Речной вокзал   ', callback_data=stations['river_station'])
    builder.button(text='🔴Студенческая    ', callback_data=stations['studentskaya'])
    builder.button(text='🔴Заельцовская    ', callback_data=stations['zaelcovska'])
    builder.button(text='🔴Октябрьская     ', callback_data=stations['octoberskaya'])
    builder.button(text='🔴Гагаринская     ', callback_data=stations['gagarinskaya'])

    builder.button(text='🟢Гарина-Михайловского', callback_data=stations['garina_mihalina'])
    builder.button(text='🟢Березовая роща      ', callback_data=stations['bereza'])
    builder.button(text='🟢Золотая нива        ', callback_data=stations['niva'])
    builder.button(text='🟢Покрышкина          ', callback_data=stations['pokrishkina'])
    builder.button(text='🟢Сибирская           ', callback_data=stations['sibirskaya'])
    builder.button(text='⬇️Назад', callback_data=callback_data['back_from_metro_callback_data'])
    builder.adjust(2)
    return builder.as_markup()


def build_choose_place(places: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i, place in enumerate(places):
        builder.button(text=f'{i+1}', callback_data=place['id'])
    builder.button(text='Назад', callback_data=callback_data['back_from_choose_place_data'])
    builder.adjust(5)
    return builder.as_markup()


def build_place_info(place_id: str, user_data: dict, dest: dict) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Показать на карте', url=f'https://2gis.ru/novosibirsk/firm/{place_id}')
    if 'metro' in user_data:
        builder.button(
            text='Построить маршрут',
            url=(
                'https://2gis.ru/novosibirsk/directions/points/{0}%2C{1}%3B{2}%7C{3}%2C{4}%3B{5}'
            ).format(
                user_data['user_loc']['lon'],
                user_data['user_loc']['lat'],
                user_data['user_loc']['id'],
                dest['lon'],
                dest['lat'],
                place_id,
            ),
        )
    else:
        builder.button(
            text='Построить маршрут',
            url='https://2gis.ru/novosibirsk/directions/points/{0}%2C{1}%7C{2}%2C{3}%3B{4}'.format(
                user_data['user_loc']['lon'],
                user_data['user_loc']['lat'],
                dest['lon'],
                dest['lat'],
                place_id,
            ),
        )

    return builder.as_markup()
