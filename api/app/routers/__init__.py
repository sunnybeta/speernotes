from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Speer Router"])

from ..routers import auth
from ..routers import note
from ..routers import search

router.include_router(auth.router, prefix="/auth", tags=["Authorization"])
router.include_router(note.router, prefix="/notes", tags=["Notes"])
router.include_router(search.router, prefix="/search", tags=["Search"])
