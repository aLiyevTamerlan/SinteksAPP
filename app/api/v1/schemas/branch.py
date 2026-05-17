from pydantic import BaseModel, Field


class BranchCreate(BaseModel):
    """Schema for creating a Branch."""
    name: str = Field(..., min_length=1, max_length=255, description="Branch name")
    brand_id: int = Field(..., description="Brand ID")
    address: str = Field(..., min_length=1, max_length=255, description="Branch address")
    is_active: bool = Field(default=True, description="Whether the branch is active")
