from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import ProductAssortment
from app.repositories.assortment import AssortmentRepository


class AssortmentService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = AssortmentRepository(session)

    async def create_assortment(self, assortment_data: dict) -> ProductAssortment:
        """Create a new assortment."""
        return await self.repository.create(assortment_data)

    async def get_assortment_by_product_and_branch(self, product_id: int, branch_id: int) -> ProductAssortment | None:
        """Get assortment for a specific product in a specific branch."""
        return await self.repository.get_by_product_and_branch(product_id, branch_id)
