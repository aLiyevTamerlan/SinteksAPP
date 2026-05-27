from __future__ import annotations  # ← ДОБАВЬ ЭТО!
from typing import TYPE_CHECKING
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.schemas.product import ProductCreate, ProductSell

from app.repositories.product import ProductRepository
from app.services.dtos.sell_context import SellContext
from app.specifications.sell.assortment_available import AssortmentAvailableSpecification
from app.specifications.sell.branch_exists import BranchExistsSpec
from app.specifications.sell.product_brand_match import ProductBrandMatchSpec
from app.specifications.sell.product_exists import ProductExistsSpec
from app.specifications.sell.stock import StockAvailableSpec, StockQuantitySpec
from app.specifications.validator import SellValidator
from app.models.product import Product
from app.services.brand import BrandService
from app.services.branch import BranchService
from app.services.assortment import AssortmentService
if TYPE_CHECKING:
    from app.services.stock import StockService
 
 
class ProductService:

 
    def __init__(
        self,
        session: AsyncSession,
        brand_service: BrandService,
        branch_service: BranchService,
        assortment_service: AssortmentService,
        stock_service: StockService,
    ):
        self.repository = ProductRepository(session)
        self.brand_service = brand_service
        self.branch_service = branch_service
        self.assortment_service = assortment_service
        self.stock_service = stock_service


    async def sell_product(self, data:ProductSell) -> Product:
        # Implementation for selling a product goes here
        product = await self.repository.get_by_id(data.product_id)
        branch = await self.branch_service.get_branch(data.branch_id)
        assortment = await self.assortment_service.get_assortment_by_product_and_branch(
            product_id=product.id,
            branch_id=branch.id,
        )
        stock = await self.stock_service.get_stock_by_product_and_branch(
            product_id=product.id,
            branch_id=branch.id,
        )
        sell_context = SellContext(
            requested_qty=data.quantity,
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
            AssortmentAvailableSpecification()
        ])
        await validator.validate(sell_context)

        
    async def create_product(self, data: ProductCreate) -> Product:

        # Validate that the brand exists and is active
        brand = await self.brand_service.get_brand(brand_id=data.brand_id)
        if not brand:
            raise ValueError(f"Brand with ID {data.brand_id} does not exist")
        if not brand.is_active:
            raise ValueError(f"Cannot create product under inactive brand {data.brand_id}")
        
        # Validate prices
        if data.purchase_price < 0:
            raise ValueError("Purchase price cannot be negative")
        if data.base_selling_price < 0:
            raise ValueError("Base selling price cannot be negative")
        if data.base_selling_price < data.purchase_price:
            raise ValueError("Base selling price must be >= purchase price")
        
        # Create product through repository
        product_data = data.model_dump()
        result = await self.repository.create(product_data=product_data)
        return result

    async def get_product(self, product_id: int) -> Product | None:
        """Get a product by ID."""
        return await self.repository.get_by_id(product_id)