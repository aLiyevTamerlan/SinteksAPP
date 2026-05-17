from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.brand import BrandRepository
from app.interfaces.sub_company_repository import ISubCompanyRepository
from app.api.v1.schemas.brand import BrandCreate
from app.models.brand import Brand


class BrandService:
    def __init__(
        self,
        session: AsyncSession,
        sub_company_repo: ISubCompanyRepository
    ):
        self.repository = BrandRepository(session)
        self.sub_company_repo = sub_company_repo

    async def create_brand(self, data: BrandCreate) -> dict:
        """Create a new brand with sub-company assignment through the service layer."""
        data_dict = data.model_dump()
        sub_company_id = data_dict.pop("sub_company_id", None)
        
        # Create brand through repository
        result = await self.repository.create(brand_data=data_dict)
        brand_id = result.id
        
        # Create brand company assignment through sub-company repository interface
        await self.repository.reassign_company(brand_id=brand_id, new_sub_company_id=sub_company_id)
        
        return result

    async def get_brand(self, brand_id: int) -> Brand | None:
        """Get a brand by ID through the repository."""
        return await self.repository.get(brand_id=brand_id)

    async def get_all_brands(self) -> list[Brand]:
        """Get all brands through the repository."""
        return await self.repository.get_all()
