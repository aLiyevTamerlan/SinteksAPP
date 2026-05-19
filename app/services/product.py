

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.api.v1.schemas.product import ProductCreate, ProductSell
from app.exceptions.branch import BranchNotFoundException
from app.exceptions.product import ProductBrandMismatchException, ProductNotAvailableInBranchException, ProductNotFoundException
from app.exceptions.stock import InsufficientStockException, OutOfStockException
from app.interfaces.brand_repository import IBrandRepository
from app.interfaces.product_repository import IProductRepository
from app.interfaces.branch_repository import IBranchRepository
from app.interfaces.assortment_repository import IAssortmentRepository
from app.interfaces.stock_repository import IStockRepository
from app.repositories.product import ProductRepository
from app.services.dtos.sell_context import SellContext
from app.specifications.sell.assortment_available import AssortmentAvailableSpecification
from app.specifications.sell.branch_exists import BranchExistsSpec
from app.specifications.sell.product_brand_match import ProductBrandMatchSpec
from app.specifications.sell.product_exists import ProductExistsSpec
from app.specifications.sell.stock import StockAvailableSpec, StockQuantitySpec
from app.specifications.validator import SellValidator
from models.product import Product
 
 
class ProductService:

 
    def __init__(
        self,
        session: AsyncSession,
        brand_repo: IBrandRepository,
        branch_repo: IBranchRepository,
        assortment_repo: IAssortmentRepository,
        stock_repo: IStockRepository,
    ):
        self.repository = ProductRepository(session)
        self.brand_repo = brand_repo
        self.branch_repo = branch_repo
        self.assortment_repo = assortment_repo
        self.stock_repo = stock_repo


    async def sell_product(self, data:ProductSell) -> Product:
        # Implementation for selling a product goes here
        product = await self.repository.get_by_id(data.product_id)
        branch = await self.branch_repo.get_by_id(data.branch_id)
        assortment = await self.assortment_repo.get_by_product_and_branch(
            product_id=product.id,
            branch_id=branch.id,
        )
        stock = await self.stock_repo.get_by_product_and_branch(
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
        brand = await self.brand_repo.get_by_id(data.brand_id)
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