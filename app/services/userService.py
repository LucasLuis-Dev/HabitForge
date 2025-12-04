from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def createUser(self, dto: UserCreate) -> User:
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
    
    async def listUsers(self) -> list[User]:
        result = await self.db.execute(select(User))
        return result.scalars().all()