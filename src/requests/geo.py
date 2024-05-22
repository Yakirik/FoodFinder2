import aiohttp
import asyncio

from pprint import pprint
from config import API_TOKEN, API_URL, TYPE, RADIUS, PAGE_SIZE


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
            'q={0}'.format(req_info['category']),
            'fields=items.point,items.reviews',
            TYPE,
            'page={0}'.format(page_number),
            PAGE_SIZE,
            'sort=distance',
            'location={0},{1}'.format(req_info['user_loc']['lon'], req_info['user_loc']['lat']),
            RADIUS,
            f'key={API_TOKEN}',
        ]
    )


async def _get_places(req_info: dict) -> list:
    async with aiohttp.ClientSession() as session:  # открытие сессии в aiohttp
        async with session.get(get_request(req_info, '1')) as resp1:
            first_page = await resp1.json()
            session.close()
            return first_page['result']['items']


async def get_places(req_info: dict) -> list:
    places = await asyncio.create_task(_get_places(req_info))
    pprint(places)
    return del_invalid_places(places)


async def main():
    task = await asyncio.create_task(_get_places())
    pprint(task)


if __name__ == '__main__':
    asyncio.run(main())
