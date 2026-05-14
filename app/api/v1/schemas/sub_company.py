from pydantic import BaseModel, Field


class SubCompanyCreate(BaseModel):
    """Schema for creating a SubCompany."""
    name: str = Field(..., min_length=1, max_length=255, description="Sub-company name")
    is_active: bool = Field(default=True, description="Whether the sub-company is active")
