from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, dto: UserCreate) -> User:
        result = await self.db.execute(select(User).where(User.email == dto.email))
        existing = result.scalar_one_or_none()
        if existing:
            raise ValueError("Email already registered")
        
        user = User(
            email=dto.email,
            hashed_password=hash_password(dto.password),
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
    
    async def get_user(self, user_id: int) -> User | None:
        result = await self.db.execute(
            select(User).where(
                User.id == user_id,
            )
        )
        return result.scalar_one_or_none()
    
    async def list_users(self) -> list[User]:
        result = await self.db.execute(select(User))
        return result.scalars().all()