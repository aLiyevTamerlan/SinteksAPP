from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.models.sub_company import SubCompany


class SubCompanyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> dict:
        """Create a new sub-company using insert statement."""
        stmt = insert(SubCompany).values(**data)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return {"id": result.lastrowid, **data}
