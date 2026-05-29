from app.exceptions.stock import InsufficientStockException, OutOfStockException
from app.shared.specifications.base import Specification


class StockAvailableSpec(Specification):
    async def is_satisfied(self, ctx):
        return ctx.stock and ctx.stock.quantity > 0

    def exception(self, ctx):
        return OutOfStockException(
            message=f"Product {ctx.product.name} stokda mövcud deyil"
        )
    
class StockQuantitySpec(Specification):
    async def is_satisfied(self, ctx):
        return ctx.stock.quantity >= ctx.requested_qty

    def exception(self, ctx):
        return InsufficientStockException(
            message=f"Stokda {ctx.stock.quantity} dənə var, {ctx.requested_qty} tələb edilir"
        )