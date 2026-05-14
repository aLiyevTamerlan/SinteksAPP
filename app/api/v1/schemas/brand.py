from pydantic import BaseModel, Field


class BrandCreate(BaseModel):
    """Schema for creating a Brand."""
    name: str = Field(..., min_length=1, max_length=255, description="Brand name")
    is_active: bool = Field(default=True, description="Whether the brand is active")
    sub_company_id: int = Field(..., description="Sub-company ID")
