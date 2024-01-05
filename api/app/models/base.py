from typing import Any
import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def create_timestamp(mapper, connection, target: Any) -> None:
    ts = datetime.datetime.now(datetime.UTC)
    target.created_at  = ts
    target.updated_at  = ts


def update_timestamp(mapper, connection, target: Any) -> None:
    ts = datetime.datetime.now(datetime.UTC)
    target.updated_at  = ts
