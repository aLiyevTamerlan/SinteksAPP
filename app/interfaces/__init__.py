"""Repository interfaces using Protocol for structural subtyping."""

from app.interfaces.assortment_repository import IAssortmentRepository
from app.interfaces.branch_repository import IBranchRepository
from app.interfaces.brand_repository import IBrandRepository
from app.interfaces.product_repository import IProductRepository
from app.interfaces.stock_repository import IStockRepository

__all__ = [
    "IAssortmentRepository",
    "IBranchRepository",
    "IBrandRepository",
    "IProductRepository",
    "IStockRepository",
]
