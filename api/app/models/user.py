from sqlalchemy import Column, event
from sqlalchemy.dialects.postgresql import TIMESTAMP, VARCHAR

from .base import Base, create_timestamp, update_timestamp

class UserModel(Base):
    __tablename__ = 'user_'

    id = Column(VARCHAR(63), nullable=False, primary_key=True)
    username = Column(VARCHAR(31), nullable=False, unique=True)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


event.listen(UserModel, 'before_insert', create_timestamp)
event.listen(UserModel, 'before_update', update_timestamp)
