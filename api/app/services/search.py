from sqlalchemy import text
from sqlalchemy.orm import Session
from ..models.note import Note

class SearchService:

    def __init__(self, db: Session) -> None:
        self.__db = db

    @staticmethod
    def _sanitize_query(query:str) -> str:
        return '|'.join(query.strip(' \n').lower().split())

    def get(self, user_id: str, query: str):
        query = self._sanitize_query(query)
        data = (
            self.
            __db.query(Note)
            .filter(
                Note.user_id == user_id,
                Note.vector.op('@@')(text(f"to_tsquery('english','{query}')"))
            )
            .all()
        )
        return data
