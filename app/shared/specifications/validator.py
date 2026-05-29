from app.services.dtos.sell_context import SellContext
from app.shared.specifications.base import Specification

class SellValidator:
    def __init__(self, specs: list[Specification[SellContext]]):
        self.specs = specs

    async def validate(self, ctx: SellContext):
        for spec in self.specs:
            if not await spec.is_satisfied(ctx):
                raise spec.exception(ctx)