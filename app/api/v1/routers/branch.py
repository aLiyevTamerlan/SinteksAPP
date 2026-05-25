from fastapi import APIRouter, Depends

from app.api.v1.schemas.branch import BranchCreate
from app.core.dependencies import get_branch_service
from app.services.branch import BranchService


router = APIRouter()

@router.post("/", status_code=201)
async def create_branch(data: BranchCreate, branch_service: BranchService = Depends(get_branch_service)):
    """Create a new branch."""
    branch = await branch_service.create_branch(data=data)
    return {"message": "Branch created successfully", "branch": branch}

@router.get("/{branch_id}")
async def get_branch(branch_id: int, branch_service: BranchService = Depends(get_branch_service)):
    """Get a branch by ID."""
    branch = await branch_service.get_branch(branch_id=branch_id)
    if not branch:
        return {"message": "Branch not found"}
    return {"branch": branch}
