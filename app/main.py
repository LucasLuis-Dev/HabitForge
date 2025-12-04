from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .database import engine
from .models.base import Base

from .routes.users import router as users_router
from .routes.habits import router as habits_router

app = FastAPI(title="HabitForge")
app.include_router(users_router)
app.include_router(habits_router)