from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import  VARCHAR

from .base import Base

class UserPass(Base):
    __tablename__ = 'user_pass_'

    user_id = Column(VARCHAR(63), ForeignKey("user_.id"), nullable=False, primary_key=True)
    salt = Column(VARCHAR(255), nullable=False)
    password = Column(VARCHAR(255), nullable=False)
