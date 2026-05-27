"""V1 API routers initialization."""
from fastapi import APIRouter

from app.api.v1.routers import sub_company, stock

router = APIRouter()

# Include sub_company router
router.include_router(sub_company.router, prefix="/sub-companies", tags=["sub-companies"])

# Include stock router
router.include_router(stock.router, prefix="/stocks", tags=["stocks"])
