from app.exceptions.product import ProductNotAvailableInBranchException
from app.services.dtos.sell_context import SellContext
from app.specifications.base import Specification


class AssortmentAvailableSpecification(Specification[SellContext]):
    async def is_satisfied(self, ctx: SellContext):
        return ctx.assortment is not None and ctx.assortment.is_active

    def exception(self, ctx: SellContext):
        return ProductNotAvailableInBranchException(
            message=f"Product {ctx.product.name} not available in branch {ctx.branch.name}"
        )