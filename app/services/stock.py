from sqlalchemy.ext.asyncio import AsyncSession
from app.models.stock import Stock
from app.repositories.stock import StockRepository
from app.repositories.branch import BranchRepository
from app.repositories.product import ProductRepository


class StockService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = StockRepository(session)
        self.branch_repository = BranchRepository(session)
        self.product_repository = ProductRepository(session)

    async def create_stock(self, stock_data: dict) -> Stock:
        """Create a new stock entry with branch and product validation."""
        branch_id = stock_data.get("branch_id")
        product_id = stock_data.get("product_id")
        
        # Validate branch exists
        branch = await self.branch_repository.get_by_id(branch_id)
        if not branch:
            raise ValueError(f"Branch with ID {branch_id} does not exist")
        
        # Validate product exists
        product = await self.product_repository.get_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} does not exist")
        
        # Create stock record
        return await self.repository.create(stock_data)

    async def get_stock_by_product_and_branch(self, product_id: int, branch_id: int) -> Stock | None:
        """Get stock entry for a specific product in a specific branch."""
        return await self.repository.get_by_product_and_branch(product_id, branch_id)

    async def decrease_stock(self, product_id: int, branch_id: int, quantity: int) -> Stock:
        """Decrease stock quantity after a sale."""
        # Get the current stock
        stock = await self.repository.get_by_product_and_branch(product_id, branch_id)
        if not stock:
            raise ValueError(f"Stock not found for Product {product_id} in Branch {branch_id}")
        
        # Check if there's enough stock
        if stock.quantity < quantity:
            raise ValueError(f"Insufficient stock. Available: {stock.quantity}, Requested: {quantity}")
        
        # Update the stock quantity
        new_quantity = stock.quantity - quantity
        updated_stock = await self.repository.update(
            stock.id,
            {"quantity": new_quantity}
        )
        return updated_stock