from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from app.interfaces.brand_repository import IBrandRepository
from app.api.v1.schemas.branch import BranchCreate
from app.models.branch import Branch
from app.repositories.branch import BranchRepository


class BranchService:
    def __init__(self, session: AsyncSession, brand_repo: IBrandRepository):
        self.repository = BranchRepository(session)
        self.brand_repo = brand_repo
 
    # Core CRUD
    async def create_branch(self, data: BranchCreate) -> Branch:
        """Create a new branch with brand validation through the service layer."""
        data_dict = data.model_dump()
        brand_id = data_dict.get("brand_id")
        
        # Validate brand existence through brand repository interface
        brand = await self.brand_repo.get_by_id(brand_id=brand_id)
        if not brand:
            ... #Add error handling for non-existent brand (e.g., raise HTTPException with 404)
        
        # Create branch through repository
        return await self.repository.create(data=data_dict)

    async def get_branch(self, branch_id: int) -> Optional[Branch]:
        """Get a branch by ID through the repository."""
        return await self.repository.get_by_id(branch_id=branch_id)