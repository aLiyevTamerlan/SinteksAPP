"""Repository interfaces using Protocol for structural subtyping."""
from typing import Protocol

from app.models.brand import Brand


class IBrandRepository(Protocol):
    """Interface for Brand repository operations."""

    async def create(self, brand_data: dict) -> Brand:
        """Create a new brand."""
        ...
        
    async def reassign_company(self, brand_id: int, new_sub_company_id: int) -> Brand:
        """Change brand's company (handles the history internally)."""
        ...

    async def get_brand(self, brand_id: int) -> Brand | None:
        """Get a brand by ID."""
        ...
