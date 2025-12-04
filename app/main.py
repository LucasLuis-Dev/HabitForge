from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .database import engine
from .models.base import Base

from .routes.users import router as usersRouter

app = FastAPI(title="HabitForge")
app.include_router(usersRouter)

# CRIA AS TABELAS (só na primeira vez)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)