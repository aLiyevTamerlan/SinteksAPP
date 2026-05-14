"""API routers initialization."""
from fastapi import APIRouter

from app.api import v1

router = APIRouter()

# Include v1 routers with v1 prefix
router.include_router(v1.router, prefix="/v1")
