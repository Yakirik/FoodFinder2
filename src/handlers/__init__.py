from aiogram import Router
from .base_commands_handlers import router as base_commands_router
from .main_menu_handlers import router as main_menu_router
from .categories_handlers import router as categories_router
from .geo_handlers import router as geo_router
from .choose_find_handlers import router as choose_find_router
from .metro_handlers import router as metro_router
from .choose_place_handlers import router as choose_place_router

router = Router()
router.include_routers(
    main_menu_router,
    categories_router,
    choose_find_router,
    geo_router,
    metro_router,
    choose_place_router,
    base_commands_router,
)
