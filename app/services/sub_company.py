from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.sub_company import SubCompanyRepository
from app.api.v1.schemas.sub_company import SubCompanyCreate


class SubCompanyService:
    def __init__(self, session: AsyncSession):
        self.repository = SubCompanyRepository(session)

    async def create_sub_company(self, data: SubCompanyCreate) -> dict:
        """Create a new sub-company through the repository."""
        return await self.repository.create(data=data.model_dump())
