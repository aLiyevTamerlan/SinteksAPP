from app.exceptions.branch import BranchNotFoundException
from app.services.dtos.sell_context import SellContext
from app.specifications.base import Specification


class BranchExistsSpec(Specification[SellContext]):
    async def is_satisfied(self, ctx: SellContext) -> bool:
        return ctx.branch is not None
    
    def exception(self, ctx: SellContext) -> BranchNotFoundException:
        return BranchNotFoundException(
            resource="Branch",
            resource_id=ctx.branch.id,
        )