from typing import Annotated
from fastapi import APIRouter, Body, Depends, Path, Request, status
from sqlalchemy.orm import Session
from ..services.note import NoteService
from ..schemas.auth import Token
from ..dependencies import get_db, get_token
from ..schemas.note import NoteForm, NoteUpdate
from ..config.slowapi import limiter
from ..exceptions import NotFound

router = APIRouter()

@router.get("", status_code=status.HTTP_200_OK)
@limiter.limit("25/minute")
def get_notes(db: Annotated[Session, Depends(get_db)], token: Annotated[Token, Depends(get_token)], request: Request):
    data = NoteService(db).get_all(token.id)
    return {'data': data}


@router.post("", status_code=status.HTTP_201_CREATED)
@limiter.limit("25/minute")
def create_note(note_form: Annotated[NoteForm, Body()], db: Annotated[Session, Depends(get_db)], token: Annotated[Token, Depends(get_token)], request: Request):
    data = NoteService(db).create(token.id, note_form)
    return {'data': data}


@router.get("/{note_id}", status_code=status.HTTP_200_OK)
@limiter.limit("25/minute")
def get_notes_by_id(note_id:Annotated[str, Path()], db: Annotated[Session, Depends(get_db)], token: Annotated[Token, Depends(get_token)], request: Request):
    data = NoteService(db).get(token.id, note_id)
    if not data:
        raise NotFound
    return {'data': data}

@router.put("/{note_id}", status_code=status.HTTP_202_ACCEPTED)
@limiter.limit("25/minute")
def update_notes_by_id(note_id:Annotated[str, Path()], note_update: NoteUpdate, db: Annotated[Session, Depends(get_db)], token: Annotated[Token, Depends(get_token)], request: Request):
    data = NoteService(db).update(user_id=token.id, note_id=note_id, note_update=note_update)
    return {'data': data}


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
@limiter.limit("25/minute")
def delete_note_by_id(note_id:Annotated[str, Path()], db: Annotated[Session, Depends(get_db)], token: Annotated[Token, Depends(get_token)], request: Request):
    NoteService(db).delete(user_id=token.id, note_id=note_id)
