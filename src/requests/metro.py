import aiohttp
import asyncio

from pprint import pprint
from config import API_TOKEN, API_URL, TYPE, PAGE_SIZE


def del_invalid_places(places: list) -> list:
    for place in places:
        try:
            place['address_name']
        except Exception:
            places.remove(place)
    return places


def get_request(req_info: dict, page_number: str) -> str:

    return API_URL + '&'.join(
        [
            'q=метро {1} {0}'.format(req_info['category'], req_info['metro']),
            'city_id=141360258613345',
            'sort=distance',
            'fields=items.point,items.reviews',
            TYPE,
            'page={0}'.format(page_number),
            PAGE_SIZE,
            f'key={API_TOKEN}',
        ]
    )


async def _get_places(req_info: dict) -> list:
    async with aiohttp.ClientSession() as session:  # открытие сессии в aiohttp
        async with session.get(get_request(req_info, '2')) as resp1:
            first_page = await resp1.json()
            return first_page['result']['items']


async def get_places(req_info: dict) -> list:
    places = await asyncio.create_task(_get_places(req_info))
    pprint(places)
    return del_invalid_places(places)
