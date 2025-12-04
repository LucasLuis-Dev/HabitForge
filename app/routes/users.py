from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(db)

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(
    dto: UserCreate,
    service: UserService = Depends(get_user_service)
):
    try:
        user = await service.create_user(dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user

@router.get("/", response_model=List[UserOut])
async def list_users(
    service: UserService = Depends(get_user_service)
):
    return await service.list_users()