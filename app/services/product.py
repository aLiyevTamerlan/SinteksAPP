

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.api.v1.schemas.product import ProductCreate
from app.interfaces.brand_repository import IBrandRepository
from app.repositories.product import ProductRepository
from models.product import Product
 
 
class ProductService:

 
    def __init__(
        self,
        session: AsyncSession,
        brand_repo: IBrandRepository
    ):
        self.repository = ProductRepository(session)
        self.brand_repo = brand_repo
 
    async def create_product(self, data: ProductCreate) -> Product:

        # Validate that the brand exists and is active
        brand = await self.brand_repo.get(data.brand_id)
        if not brand:
            raise ValueError(f"Brand with ID {data.brand_id} does not exist")
        if not brand.is_active:
            raise ValueError(f"Cannot create product under inactive brand {data.brand_id}")
        
        # Validate prices
        if data.purchase_price < 0:
            raise ValueError("Purchase price cannot be negative")
        if data.base_selling_price < 0:
            raise ValueError("Base selling price cannot be negative")
        if data.base_selling_price < data.purchase_price:
            raise ValueError("Base selling price must be >= purchase price")
        
        # Create product through repository
        product_data = data.model_dump()
        result = await self.repository.create(product_data=product_data)
        return result