import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Postgres:
    user     = os.getenv("POSTGRES_USER","Kentaro")
    password = os.getenv("POSTGRES_PASSWORD","Toji")
    host     = os.getenv("POSTGRES_HOST", "Hanagaki")
    port     = os.getenv("POSTGRES_PORT", int(5432))
    database = os.getenv("POSTGRES_DB", "Midoriya")
    
    @property
    def url(self):
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

engine = create_engine(Postgres().url, connect_args={})
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
