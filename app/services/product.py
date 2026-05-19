

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.api.v1.schemas.product import ProductCreate, ProductSell
from app.interfaces.brand_repository import IBrandRepository
from app.interfaces.product_repository import IProductRepository
from app.interfaces.branch_repository import IBranchRepository
from app.interfaces.assortment_repository import IAssortmentRepository
from app.interfaces.stock_repository import IStockRepository
from app.repositories.product import ProductRepository
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
        if not product:
            raise ProductNotFound(
                f"Product ID {data.product_id} tapılmadı"
            )
        branch = await self.branch_repo.get_by_id(data.branch_id)
        if not branch:
            raise BranchNotFound(
                f"Branch ID {data.branch_id} tapılmadı"
            )
        if product.brand_id != branch.brand_id:
            raise ProductBrandMismatch(
                f"Product (Brand {product.brand_id}) bu branchə "
                f"(Brand {branch.brand_id}) aid deyil"
            )
        assortment = await self.assortment_repo.get_by_product_and_branch(
            product_id=product.id,
            branch_id=branch.id,
        )
        if not assortment or not assortment.is_active:
            raise ProductNotAvailableInBranch(
                f"Product {product.name} bu branchda mövcud deyil/aktiv deyil"
            )
        stock = await self.stock_repo.get_by_product_and_branch(
            product_id=product.id,
            branch_id=branch.id,
        )
        if not stock or stock.quantity <= 0:
            raise OutOfStock(
                f"Product {product.name} stokda mövcud deyil"
            )
        if stock.quantity < data.requested_qty:
            raise InsufficientStock(
                f"Stokda {stock.quantity} dənə var, "
                f"{data.requested_qty} dənə tələb edilir"
            )
        
    async def create_product(self, data: ProductCreate) -> Product:

        # Validate that the brand exists and is active
        brand = await self.brand_repo.get_by_id(data.brand_id)
        if not brand:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Brand with ID {data.brand_id} does not exist"
            )
        if not brand.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Cannot create product under inactive brand {data.brand_id}"
            )
        
        # Validate prices
        if data.purchase_price < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Purchase price cannot be negative"
            )
        if data.base_selling_price < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Base selling price cannot be negative"
            )
        if data.base_selling_price < data.purchase_price:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Base selling price must be >= purchase price"
            )
        
        # Create product through repository
        product_data = data.model_dump()
        result = await self.repository.create(product_data=product_data)
        return result