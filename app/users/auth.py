from passlib.context import CryptContext
from pydantic import EmailStr
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.config import get_auth_data
from app.users.dao import UsersDAO


