"""Repository interface for Product operations."""
from typing import Protocol

from app.models.product import Product


class IProductRepository(Protocol):
    """Interface for Product repository operations."""

    async def create(self, product_data: dict) -> Product:
        """Create a new product."""
        ...

    async def get_by_id(self, product_id: int) -> Product | None:
        """Get a product by ID."""
        ...

    async def get_all(self) -> list[Product]:
        """Get all products."""
        ...

    async def update(self, product_id: int, product_data: dict) -> Product:
        """Update a product."""
        ...

    async def delete(self, product_id: int) -> bool:
        """Delete a product."""
        ...
