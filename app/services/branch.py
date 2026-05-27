from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.schemas.branch import BranchCreate
from app.models.branch import Branch
from app.repositories.branch import BranchRepository
from app.services.brand import BrandService


class BranchService:
    def __init__(self, session: AsyncSession, brand_service: BrandService):
        self.repository = BranchRepository(session)
        self.brand_service = brand_service
 
    # Core CRUD
    async def create_branch(self, data: BranchCreate) -> Branch:
        """Create a new branch with brand validation through the service layer."""
        data_dict = data.model_dump()
        brand_id = data_dict.get("brand_id")
        
        # Validate brand existence through brand service
        brand = await self.brand_service.get_brand(brand_id=brand_id)
        if not brand:
            raise ValueError(f"Brand with ID {brand_id} does not exist")
        
        # Create branch through repository
        return await self.repository.create(data=data_dict)

    async def get_branch(self, branch_id: int) -> Optional[Branch]:
        """Get a branch by ID through the repository."""
        return await self.repository.get_by_id(branch_id=branch_id)