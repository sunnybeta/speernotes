from typing import Annotated
from fastapi import APIRouter, Depends, Body, HTTPException, Request, status
from sqlalchemy.orm import Session
from ..services.auth import AuthService
from ..schemas.auth import SignupForm, LoginForm
from ..dependencies import get_db
from ..config.slowapi import limiter

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED)
@limiter.limit("20/minute")
def signup(
    signup_form: Annotated[SignupForm, Body()], 
    db: Annotated[Session, Depends(get_db)],
    request: Request,
):
    data = AuthService(db).signup(signup_form)
    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This username / password already exists")
    return {'data': data}

@router.post("/login", status_code=status.HTTP_200_OK)
@limiter.limit("20/minute")
def login(
    login_form: Annotated[LoginForm, Body()],
    db: Annotated[Session, Depends(get_db)],
    request: Request,
):
    token = AuthService(db).login(login_form)
    if not token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
    return {'data':{'token':token}}
