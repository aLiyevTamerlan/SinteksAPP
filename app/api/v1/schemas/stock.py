from pydantic import BaseModel, Field


class StockCreate(BaseModel):
    """Schema for creating a Stock entry."""
    branch_id: int = Field(..., description="Branch ID")
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Stock quantity")


class StockResponse(BaseModel):
    """Schema for Stock response."""
    id: int
    branch_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True
