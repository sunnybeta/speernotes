import os
from dotenv import load_dotenv

load_dotenv()

origins = {
    "dev": ["*"],
    "prod": ["*"],
}

class Base:
    env = os.getenv("ENVIRONMENT", "dev")
    name = os.getenv("NAME")
    url = os.getenv("URL")
    origins = origins.get(env)
