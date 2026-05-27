from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.brand import BrandRepository
from app.api.v1.schemas.brand import BrandCreate
from app.models.brand import Brand
from app.services.sub_company import SubCompanyService


class BrandService:
    def __init__(
        self,
        session: AsyncSession,
        sub_company_service: SubCompanyService
    ):
        self.repository = BrandRepository(session)
        self.sub_company_service = sub_company_service

    async def create_brand(self, data: BrandCreate) -> dict:
        """Create a new brand with sub-company assignment through the service layer."""
        data_dict = data.model_dump()
        sub_company_id = data_dict.pop("sub_company_id", None)
        
        # Validate that the sub-company exists through the sub-company service
        if sub_company_id:
            sub_company = await self.sub_company_service.get_sub_company(sub_company_id)
            if not sub_company:
                raise ValueError(f"SubCompany with ID {sub_company_id} does not exist")
        
        # Create brand through repository
        result = await self.repository.create(brand_data=data_dict)
        brand_id = result.id
        
        # Create brand company assignment through repository
        await self.repository.reassign_company(brand_id=brand_id, new_sub_company_id=sub_company_id)
        
        return result

    async def get_brand(self, brand_id: int) -> Brand | None:
        """Get a brand by ID through the repository."""
        return await self.repository.get_by_id(brand_id=brand_id)
