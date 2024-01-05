from .services.auth import AuthService
from .config.postgres import session_local
from typing import Annotated
from fastapi import Header

def get_db():
    db = session_local()
    try:
        return db
    finally:
        db.close()


def get_token(authorization: Annotated[str, Header()]):
    token = authorization.replace("Bearer ",'')
    return AuthService.decode(token)
