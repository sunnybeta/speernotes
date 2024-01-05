from sqlalchemy import func
from ..schemas.note import NoteForm, NoteUpdate
from ..models.note import Note
from .servicemixin import ServiceMixin

class NoteService(ServiceMixin):

    def __init__(self, db) -> None:
        self.__db = db

    def get_all(self, user_id: str):
        return self.__db.query(Note).filter(Note.user_id == user_id).all()

    def get(self, user_id: str, note_id: str):
        return self.__db.query(Note).filter(Note.user_id == user_id, Note.id == note_id).first()

    def create(self, user_id: str, note_form: NoteForm):
        note_id = self.generate_id(prefix="not")
        note = Note(
            **note_form.model_dump(),
            id=note_id,
            user_id=user_id,
            vector=func.to_tsvector(note_form.content)
        )
        self.__db.execute(Note.__table__.insert().values([dict(**note_form.model_dump(), id=note_id, user_id=user_id, vector=func.to_tsvector(note_form.content), created_at=func.now(), updated_at=func.now())]))
        self.__db.commit()
        return Note(
            **note_form.model_dump(),
            id=note_id,
            user_id=user_id,
        )

    def update(self, user_id: str, note_id: str, note_update: NoteUpdate):
        note = self.__db.query(Note).filter(Note.user_id == user_id, Note.id == note_id).first()
        setattr(note, "title", note_update.title)
        setattr(note, "content", note_update.content)
        self.__db.commit()
        self.__db.refresh(note)
        return note

    def delete(self, user_id: str, note_id: str):
        self.__db.query(Note).filter(Note.user_id == user_id, Note.id == note_id).delete()
        self.__db.commit()
