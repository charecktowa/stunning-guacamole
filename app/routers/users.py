from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_setup import get_db

from schemas.user import User, UserCreate, UserLogin
import utils.users

from auth.jwt_handler import signJWT

router = APIRouter(prefix="/user", tags=["users"])

# User SignUp [ create a new user ]
@router.post("/user/signup", response_model=User)
async def user_signup(user: UserCreate, db: Session = Depends(get_db)):
    if db_user := utils.users.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    return utils.users.create_user(db=db, user=user)


@router.post("/user/login")
async def user_login(user: UserLogin, db: Session = Depends(get_db)):
    if check_user(user=user, db=db) == True:
        return signJWT(user.email)

    raise HTTPException(status_code=400, detail="Credenciales invalidas")


def check_user(user: UserLogin, db: Session = Depends(get_db)):
    if utils.users.get_user_by_email(db, user.email):
        # check password
        password = utils.users.get_user_with_password(db, user.email)
        if user.password == password.password:
            print(user.password, password.password)
            return True
    return False
