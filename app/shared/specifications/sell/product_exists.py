from app.exceptions.product import ProductNotFoundException
from app.services.dtos.sell_context import SellContext
from app.shared.specifications.base import Specification


class ProductExistsSpec(Specification[SellContext]):
    async def is_satisfied(self, ctx: SellContext) -> bool:
        return ctx.product is not None
    
    def exception(self, ctx: SellContext) -> ProductNotFoundException:
        return ProductNotFoundException(
            resource="Product",
            resource_id=ctx.product.id,
        )