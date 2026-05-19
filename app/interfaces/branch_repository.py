"""Repository interface for Branch operations."""
from typing import Protocol

from app.models.branch import Branch


class IBranchRepository(Protocol):
    """Interface for Branch repository operations."""

    async def create(self, branch_data: dict) -> Branch:
        """Create a new branch."""
        ...

    async def get(self) -> list[Branch]:
        """Get all branches."""
        ...

    async def get_by_id(self, branch_id: int) -> Branch | None:
        """Get a branch by ID."""
        ...

    async def update(self, branch_id: int, branch_data: dict) -> Branch:
        """Update a branch."""
        ...

    async def delete(self, branch_id: int) -> bool:
        """Delete a branch."""
        ...
