

from app.commands.sell_product import SellProductCommand
from app.repositories.product import ProductRepository
from app.services.dtos.sell_context import SellContext
from app.shared.specifications.sell import *
from app.shared.specifications.validator import SellValidator


class SellProductHandler:

    def __init__(
        self,
        repository: ProductRepository,
        branch_service,
        assortment_service,
        stock_service,
    ):
        self.repository = repository
        self.branch_service = branch_service
        self.assortment_service = assortment_service
        self.stock_service = stock_service

    async def handle(
        self,
        command: SellProductCommand
    ):

        product = await self.repository.get_by_id(
            command.product_id
        )

        branch = await self.branch_service.get_branch(
            command.branch_id
        )

        assortment = (
            await self.assortment_service
            .get_assortment_by_product_and_branch(
                product_id=command.product_id,
                branch_id=command.branch_id,
            )
        )

        stock = (
            await self.stock_service
            .get_stock_by_product_and_branch(
                product_id=command.product_id,
                branch_id=command.branch_id,
            )
        )

        sell_context = SellContext(
            requested_qty=command.quantity,
            product=product,
            branch=branch,
            assortment=assortment,
            stock=stock,
        )

        validator = SellValidator([
            ProductExistsSpec(),
            BranchExistsSpec(),
            ProductBrandMatchSpec(),
            StockAvailableSpec(),
            StockQuantitySpec(),
            AssortmentAvailableSpecification(),
        ])

        await validator.validate(sell_context)

        await self.stock_service.decrease_stock(
            product_id=command.product_id,
            branch_id=command.branch_id,
            quantity=command.quantity,
        )

        return {
            "message": "Product sold successfully"
        }