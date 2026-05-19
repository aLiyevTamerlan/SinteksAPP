"""Repository interface for Product Assortment operations."""
from typing import Protocol

from app.models.product import ProductAssortment


class IAssortmentRepository(Protocol):
    """Interface for Product Assortment repository operations."""

    async def create(self, assortment_data: dict) -> ProductAssortment:
        """Create a new product assortment."""
        ...

    async def get_by_id(self, assortment_id: int) -> ProductAssortment | None:
        """Get an assortment by ID."""
        ...

    async def get_all(self) -> list[ProductAssortment]:
        """Get all assortments."""
        ...

    async def get_by_product(self, product_id: int) -> list[ProductAssortment]:
        """Get assortments for a specific product."""
        ...

    async def get_by_branch(self, branch_id: int) -> list[ProductAssortment]:
        """Get assortments for a specific branch."""
        ...

    async def update(self, assortment_id: int, assortment_data: dict) -> ProductAssortment:
        """Update an assortment."""
        ...

    async def delete(self, assortment_id: int) -> bool:
        """Delete an assortment."""
        ...
