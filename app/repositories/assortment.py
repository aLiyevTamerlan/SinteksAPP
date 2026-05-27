from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, update, delete
from app.models.product import ProductAssortment


class AssortmentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, assortment_data: dict) -> ProductAssortment:
        """Create a new product assortment."""
        stmt = insert(ProductAssortment).values(**assortment_data).returning(ProductAssortment)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()
    
    async def get_by_id(self, assortment_id: int) -> ProductAssortment | None:
        """Get an assortment by ID."""
        stmt = select(ProductAssortment).where(ProductAssortment.id == assortment_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all(self) -> list[ProductAssortment]:
        """Get all assortments."""
        stmt = select(ProductAssortment)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_product(self, product_id: int) -> list[ProductAssortment]:
        """Get assortments for a specific product."""
        stmt = select(ProductAssortment).where(ProductAssortment.product_id == product_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_branch(self, branch_id: int) -> list[ProductAssortment]:
        """Get assortments for a specific branch."""
        stmt = select(ProductAssortment).where(ProductAssortment.branch_id == branch_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_product_and_branch(self, product_id: int, branch_id: int) -> ProductAssortment | None:
        """Get assortment for a specific product in a specific branch."""
        stmt = select(ProductAssortment).where(
            (ProductAssortment.product_id == product_id) & (ProductAssortment.branch_id == branch_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, assortment_id: int, assortment_data: dict) -> ProductAssortment:
        """Update an assortment."""
        stmt = update(ProductAssortment).where(
            ProductAssortment.id == assortment_id
        ).values(**assortment_data).returning(ProductAssortment)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete(self, assortment_id: int) -> bool:
        """Delete an assortment."""
        stmt = delete(ProductAssortment).where(ProductAssortment.id == assortment_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0
