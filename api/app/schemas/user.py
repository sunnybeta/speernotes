from datetime import datetime
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: str
    name: str
    email: str
    username: str
    created_at: datetime
    updated_at: datetime
