from fastapi import APIRouter

from app.api import items, users, utils, jinja_test

api_router = APIRouter()

api_router.include_router(utils.router, tags=["utils"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(items.router, tags=["items"])
api_router.include_router(jinja_test.router, tags=["jinja_test"])
