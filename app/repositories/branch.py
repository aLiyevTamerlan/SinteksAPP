from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from app.models.branch import Branch


class BranchRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self) -> list[Branch]:
        """Get all branches."""
        stmt = select(Branch)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_id(self, branch_id: int) -> Branch | None:
        """Get a branch by ID."""
        stmt = select(Branch).where(Branch.id == branch_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, data: dict) -> Branch:
        """Create a new branch."""
        stmt = insert(Branch).values(**data).returning(Branch)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()
