from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.services.userService import UserService

router = APIRouter(prefix="/users", tags=["users"])

def getUserService(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(db)

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def createUser(
    dto: UserCreate,
    service: UserService = Depends(getUserService)
):
    try:
        print(dto)
        user = await service.createUser(dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user

@router.get("/", response_model=List[UserOut])
async def listUsers(
    service: UserService = Depends(getUserService)
):
    return await service.listUsers()