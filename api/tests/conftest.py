from pytest import fixture
from app.asgi import app
from fastapi.testclient import TestClient
from app.models.base import Base
from app.models.user import UserModel
from app.schemas.auth import Token
from app.dependencies import get_db, get_token
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})
TestingSessionLocal = sessionmaker(autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_token():
    return Token(id="usr_t35t3r", username="rainmain", email="shady@aftermath.com")

@fixture(scope="session")
def client():
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_token] = override_get_token
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    user = UserModel(id="usr_t35t3r", username="rainman", email="shady@aftermath.com")
    db.add(user)
    db.commit()
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)
