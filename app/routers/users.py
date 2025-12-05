from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies.auth import get_current_user
from app.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(db)


@router.get("/{user_id}", response_model=UserOut)
async def get_user(
    user_id: int,   
    service: UserService = Depends(get_user_service),
):
    user = await service.get_user(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Habit not found")
    return user

@router.get("/", response_model=List[UserOut])
async def list_users(
    service: UserService = Depends(get_user_service)
):
    return await service.list_users()