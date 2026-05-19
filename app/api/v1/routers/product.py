from fastapi import APIRouter, Depends

from app.api.v1.schemas.product import ProductCreate
from app.core.dependencies import get_product_service
from app.services.product import ProductService


router = APIRouter()

@router.post("/", status_code=201)
async def create_product(data: ProductCreate, product_service: ProductService = Depends(get_product_service)):
    """Create a new product."""
    await product_service.create_product(data=data)
    # Implementation for creating a product goes here
    return {"message": "Product created successfully"}

@router.post("/sell")
async def sell_product(data: ProductCreate, product_service: ProductService = Depends(get_product_service)):
    """Sell a product."""
    await product_service.sell_product(data=data)
    # Implementation for selling a product goes here
    return {"message": "Product sold successfully"}
