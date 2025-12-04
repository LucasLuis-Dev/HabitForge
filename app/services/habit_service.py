from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.habits import Habit
from app.schemas.habit import HabitCreate


class HabitService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_habit(self, user_id: int, payload: HabitCreate) -> Habit:
        habit = Habit(
            user_id=user_id,
            name=payload.name,
            frequency=payload.frequency,
            target_reps=payload.target_reps,
        )
        self.db.add(habit)
        await self.db.commit()
        await self.db.refresh(habit)
        return habit

    async def list_habits(self, user_id: int) -> list[Habit]:
        result = await self.db.execute(
            select(Habit).where(Habit.user_id == user_id)
        )
        return result.scalars().all()

    async def get_habit(self, user_id: int, habit_id: int) -> Habit | None:
        result = await self.db.execute(
            select(Habit).where(
                Habit.user_id == user_id,
                Habit.id == habit_id,
            )
        )
        return result.scalar_one_or_none()

    async def delete_habit(self, user_id: int, habit_id: int) -> bool:
        habit = await self.get_habit(user_id, habit_id)
        if not habit:
            return False

        await self.db.delete(habit)
        await self.db.commit()
        return True
