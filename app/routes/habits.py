from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.habit import HabitCreate, HabitOut
from app.services.habit_service import HabitService

router = APIRouter(prefix="/habits", tags=["habits"])


def get_habit_service(db: AsyncSession = Depends(get_db)) -> HabitService:
    return HabitService(db)


FAKE_USER_ID = 1


@router.post("/", response_model=HabitOut, status_code=status.HTTP_201_CREATED)
async def create_habit(
    payload: HabitCreate,
    service: HabitService = Depends(get_habit_service),
):
    habit = await service.create_habit(user_id=FAKE_USER_ID, payload=payload)
    return habit


@router.get("/", response_model=List[HabitOut])
async def list_habits(
    service: HabitService = Depends(get_habit_service),
):
    habits = await service.list_habits(user_id=FAKE_USER_ID)
    return habits


@router.get("/{habit_id}", response_model=HabitOut)
async def get_habit(
    habit_id: int,
    service: HabitService = Depends(get_habit_service),
):
    habit = await service.get_habit(user_id=FAKE_USER_ID, habit_id=habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit


@router.delete("/{habit_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_habit(
    habit_id: int,
    service: HabitService = Depends(get_habit_service),
):
    deleted = await service.delete_habit(user_id=FAKE_USER_ID, habit_id=habit_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Habit not found")
    return None
