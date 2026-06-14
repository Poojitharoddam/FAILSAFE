from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt

router = APIRouter(prefix="/auth", tags=["Authentication"])

# ==========================
# JWT Config
# ==========================

SECRET_KEY = "failsafe_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# ==========================
# Dummy User Database
# ==========================

users_db = {
    "faculty@failsafe.com": {
        "password": "admin123"
    }
}

# ==========================
# Request Models
# ==========================

class LoginRequest(BaseModel):
    email: str
    password: str


# ==========================
# JWT Token Generator
# ==========================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# ==========================
# Login Endpoint
# ==========================

@router.post("/login")
def login(user: LoginRequest):

    db_user = users_db.get(user.email)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email"
        )

    if db_user["password"] != user.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "message": "Login Successful",
        "access_token": token,
        "token_type": "bearer"
    }


# ==========================
# Register Endpoint
# ==========================

@router.post("/register")
def register(user: LoginRequest):

    if user.email in users_db:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    users_db[user.email] = {
        "password": user.password
    }

    return {
        "message": "User Registered Successfully"
    }