from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from ..api import Pagination

class NoteForm(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    content: str
    title: str

class Note(NoteForm):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    created_at: datetime
    created_at: datetime

class NoteUpdate(NoteForm):
    ...

class NoteResponse(BaseModel):
    data: Note | List[Note]
    pagination: Optional[Pagination] = None
