from app.exceptions.product import ProductBrandMismatchException
from app.services.dtos.sell_context import SellContext
from app.specifications.base import Specification


class ProductBrandMatchSpec(Specification[SellContext]):
    async def is_satisfied(self, ctx: SellContext) -> bool:
        return ctx.product.brand_id == ctx.branch.id

    def exception(self, ctx: SellContext) -> ProductBrandMismatchException:
        return ProductBrandMismatchException(
            message=f"Product {ctx.product.name} not belongs to branch {ctx.branch.id}"
        )