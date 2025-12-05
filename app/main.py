from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .database import engine
from .models.base import Base

from .routers.auth import router as auth_router
from .routers.users import router as users_router
from .routers.habits import router as habits_router

app = FastAPI(
    title="HabitForge",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

from .routers.auth import router as auth_router
from .routers.users import router as users_router
from .routers.habits import router as habits_router

app.include_router(auth_router, prefix="/api")
app.include_router(users_router, prefix="/api")
app.include_router(habits_router, prefix="/api")