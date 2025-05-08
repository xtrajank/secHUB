'''
secHUB // backend // api // __init__.py
Description: Combines all the routers into one file to be used in main.py
'''
from fastapi import APIRouter
from firemon import router as firemon_router
#from .system_health import router as health_router
#from .logs import router as logs_router

router = APIRouter()
router.include_router(firemon_router)
#router.include_router(health_router)
#router.include_router(logs_router)
