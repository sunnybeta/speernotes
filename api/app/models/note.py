from sqlalchemy import Column, ForeignKey, event
from sqlalchemy.dialects.postgresql import TIMESTAMP, TSVECTOR, VARCHAR

from .base import Base, create_timestamp, update_timestamp

class Note(Base):
    __tablename__ = 'note_'

    id = Column(VARCHAR(63), nullable=False, primary_key=True)
    user_id = Column(VARCHAR(63), ForeignKey("user_.id"), nullable=False)
    title = Column(VARCHAR(127), nullable=False)
    content = Column(VARCHAR(1023), nullable=False)
    vector = Column(TSVECTOR)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

event.listen(Note, 'before_insert', create_timestamp)
event.listen(Note, 'before_update', update_timestamp)
