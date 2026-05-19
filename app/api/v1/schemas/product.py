from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    """Schema for creating a Product."""
    name: str = Field(..., min_length=1, max_length=255, description="Product name")
    category_id: int = Field(..., description="Product category ID")
    color: str = Field(..., min_length=1, max_length=255, description="Product color")
    size: float = Field(..., description="Product size")
    purchase_price: float = Field(..., gt=0, description="Purchase price")
    base_selling_price: float = Field(..., gt=0, description="Base selling price")
    is_active: bool = Field(default=True, description="Whether the product is active")


class ProductSell(BaseModel):
    """Schema for selling a Product."""
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity to sell")
    selling_price: float = Field(..., gt=0, description="Selling price per unit")
    branch_id: int = Field(..., description="Branch ID")
    discount: float = Field(default=0, ge=0, le=100, description="Discount percentage (0-100)")
