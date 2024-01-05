from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from .config.slowapi import limiter
from .config.base import Base
from .routers import router

app = FastAPI(description="Speer Notes API", redoc_url="/_internal_/docs")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=Base.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/healthcheck", status_code=status.HTTP_200_OK)
async def healthcheck():
    return {'status':'healthy'}
