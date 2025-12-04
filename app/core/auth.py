from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from jwt import InvalidTokenError
from pydantic import BaseModel

from app.core.security import verify_password
from app.models.user import User
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> TokenData:
    try:
        dto = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = dto.get("sub")
        if user_id is None:
            raise InvalidTokenError("Missing subject")
        return TokenData(user_id=int(user_id))
    except InvalidTokenError as e:
        raise e


def authenticate_user(user: User | None, password: str) -> User | None:
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
