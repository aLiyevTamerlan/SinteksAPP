"""Repository interface for Stock operations."""
from typing import Protocol

from app.models.stock import Stock


class IStockRepository(Protocol):
    """Interface for Stock repository operations."""

    async def create(self, stock_data: dict) -> Stock:
        """Create a new stock entry."""
        ...

    async def get_by_id(self, stock_id: int) -> Stock | None:
        """Get a stock entry by ID."""
        ...

    async def get_all(self) -> list[Stock]:
        """Get all stock entries."""
        ...

    async def get_by_product(self, product_id: int) -> list[Stock]:
        """Get all stock entries for a product."""
        ...

    async def get_by_branch(self, branch_id: int) -> list[Stock]:
        """Get all stock entries in a branch."""
        ...

    async def get_by_product_and_branch(self, product_id: int, branch_id: int) -> Stock | None:
        """Get stock entry for a specific product in a specific branch."""
        ...

    async def update(self, stock_id: int, stock_data: dict) -> Stock:
        """Update a stock entry."""
        ...

    async def delete(self, stock_id: int) -> bool:
        """Delete a stock entry."""
        ...
