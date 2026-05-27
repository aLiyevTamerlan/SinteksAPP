from sqlalchemy.ext.asyncio import AsyncSession
from app.models.stock import Stock
from app.repositories.stock import StockRepository
from app.services.branch import BranchService
from app.services.product import ProductService


class StockService:
    def __init__(
        self,
        session: AsyncSession,
        branch_service: BranchService,
        product_service: ProductService,
    ):
        self.session = session
        self.repository = StockRepository(session)
        self.branch_service = branch_service
        self.product_service = product_service

    async def create_stock(self, stock_data: dict) -> Stock:
        """Create a new stock entry with branch and product validation."""
        branch_id = stock_data.get("branch_id")
        product_id = stock_data.get("product_id")
        
        # Validate branch exists
        branch = await self.branch_service.get_branch(branch_id)
        if not branch:
            raise ValueError(f"Branch with ID {branch_id} does not exist")
        
        # Validate product exists
        product = await self.product_service.get_product(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} does not exist")
        
        # Create stock record
        return await self.repository.create(stock_data)