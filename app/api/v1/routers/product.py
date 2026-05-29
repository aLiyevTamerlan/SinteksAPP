from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.schemas.product import ProductCreate
from app.commands.sell_product import SellProductCommand
from app.core.database.session import get_db
from app.core.dependencies import get_product_service
from app.handlers.sell_product import SellProductHandler
from app.repositories.product import ProductRepository
from app.services.assortment import AssortmentService
from app.services.product import ProductService
from app.services.stock import StockService
from app.shared.mediator import Mediator


router = APIRouter()

@router.post("/", status_code=201)
async def create_product(data: ProductCreate, product_service: ProductService = Depends(get_product_service)):
    """Create a new product."""
    await product_service.create_product(data=data)
    # Implementation for creating a product goes here
    return {"message": "Product created successfully"}

@router.post("/sell")
async def sell_product(command: SellProductCommand, 
                       session: AsyncSession = Depends(get_db),
):
    """Sell a product."""
    handler = SellProductHandler(
        repository=ProductRepository(session),
        stock_service=StockService(session),
        assortment_service=AssortmentService(session),
    )

    mediator = Mediator()
    mediator.register(SellProductCommand, handler)
    await mediator.send(command)
    # Implementation for selling a product goes here
    return {"message": "Product sold successfully"}
