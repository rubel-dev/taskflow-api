from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.user import UserCreate, UserLogin
from app.core.security import create_access_token, hashed_password, verify_password
from app.models.user import User

router = APIRouter()

@router.post('/register')
def register(
    user: UserCreate,
    db:Session = Depends(get_db)
):
    hashed_pw = hashed_password(user.password)
    new_user = User(
        username = user.username,
        email = user.email,
        password = hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message":"User created"
    }

@router.post('/login')
def login(
    user: UserLogin,
    db:Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(
            status_code = 401,
            detail = "Invalied Credentials"
        )
    valid_password = verify_password(user.password, db_user.password)
    
    if not valid_password:
        raise HTTPException(
            status_code=401,
            detail = 'Invalid Credentials'
        )
    token = create_access_token(
        data = {
            "user_id":db_user.id
        }
    )
    return {
        "access_token":token,
        "token_type":"bearer"
    }
