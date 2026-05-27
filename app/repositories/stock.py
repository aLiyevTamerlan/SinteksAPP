from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, update, delete
from app.models.stock import Stock


class StockRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, stock_data: dict) -> Stock:
        """Create a new stock entry."""
        stmt = insert(Stock).values(**stock_data).returning(Stock)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()
    
    async def get_by_id(self, stock_id: int) -> Stock | None:
        """Get a stock entry by ID."""
        stmt = select(Stock).where(Stock.id == stock_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Stock]:
        """Get all stock entries."""
        stmt = select(Stock)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_product(self, product_id: int) -> list[Stock]:
        """Get all stock entries for a product."""
        stmt = select(Stock).where(Stock.product_id == product_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_branch(self, branch_id: int) -> list[Stock]:
        """Get all stock entries in a branch."""
        stmt = select(Stock).where(Stock.branch_id == branch_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_product_and_branch(self, product_id: int, branch_id: int) -> Stock | None:
        """Get stock entry for a specific product in a specific branch."""
        stmt = select(Stock).where(
            (Stock.product_id == product_id) & (Stock.branch_id == branch_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, stock_id: int, stock_data: dict) -> Stock:
        """Update a stock entry."""
        stmt = update(Stock).where(Stock.id == stock_id).values(**stock_data).returning(Stock)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete(self, stock_id: int) -> bool:
        """Delete a stock entry."""
        stmt = delete(Stock).where(Stock.id == stock_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0
