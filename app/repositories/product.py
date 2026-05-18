from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.models.product import Product


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, product_data: dict) -> Product:
        """Create a new product."""
        stmt = insert(Product).values(**product_data).returning(Product)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()