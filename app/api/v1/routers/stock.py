from fastapi import APIRouter, Depends, status

from app.api.v1.schemas.stock import StockCreate, StockResponse
from app.core.dependencies import get_stock_service
from app.services.stock import StockService


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=StockResponse)
async def create_stock(
    data: StockCreate,
    stock_service: StockService = Depends(get_stock_service)
):
    """Create a new stock entry."""
    stock = await stock_service.create_stock(data.model_dump())
    return stock
