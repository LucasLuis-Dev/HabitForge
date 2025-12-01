from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .database import engine, get_db
from .models.base import Base
from .models.user import User
from .models.habits import Habit

app = FastAPI(title="HabitForge")

# CRIA AS TABELAS (só na primeira vez)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return {"message": "HabitForge rodando!", "users": len(users)}
