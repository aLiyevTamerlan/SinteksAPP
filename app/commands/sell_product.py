from pydantic import BaseModel, Field

class SellProductCommand(BaseModel):
    """Schema for selling a Product."""
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity to sell")
    selling_price: float = Field(..., gt=0, description="Selling price per unit")
    branch_id: int = Field(..., description="Branch ID")
    discount: float = Field(default=0, ge=0, le=100, description="Discount percentage (0-100)")