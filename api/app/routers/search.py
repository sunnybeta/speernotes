from typing import Annotated
from fastapi import APIRouter, Query, Depends, Request
from sqlalchemy.orm import Session
from ..schemas.auth import Token
from ..services.search import SearchService
from ..dependencies import get_token, get_db
from ..config.slowapi import limiter

router = APIRouter()

@router.get("")
@limiter.limit("40/minute")
def search_notes(
    q: Annotated[str, Query()],
    token: Annotated[Token, Depends(get_token)],
    db: Annotated[Session, Depends(get_db)],
    request: Request,
):
    data = SearchService(db).get(user_id=token.id, query=q)
    return {'data':data}
