"""Repository interfaces using Protocol for structural subtyping."""
from typing import Protocol

from app.models.sub_company import SubCompany


class ISubCompanyRepository(Protocol):
    """Interface for SubCompany repository operations."""

    async def create(self, data: dict) -> dict:
        """Create a new sub-company."""
        ...
        
    async def get(self, sub_company_id: int) -> SubCompany | None:
        """Get a sub-company by ID."""
        ...