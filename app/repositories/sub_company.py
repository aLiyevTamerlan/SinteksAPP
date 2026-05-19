from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from app.models.sub_company import SubCompany


class SubCompanyRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, sub_company_id: int) -> SubCompany | None:
        """Get a sub-company by ID."""
        stmt = select(SubCompany).where(SubCompany.id == sub_company_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    async def create(self, data: dict) -> SubCompany:
        """Create a new sub-company."""
        stmt = insert(SubCompany).values(**data).returning(SubCompany)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()
