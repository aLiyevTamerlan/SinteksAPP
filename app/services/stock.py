from sqlalchemy.ext.asyncio import AsyncSession
from app.models.stock import Stock
from app.repositories.stock import StockRepository


class StockService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = StockRepository(session)

    async def create_stock(self, stock_data: dict) -> Stock:
        """Create a new stock entry."""
        return await self.repository.create(stock_data)
