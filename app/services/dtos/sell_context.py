from dataclasses import dataclass

from app.models.branch import Branch
from app.models.product import Product, ProductAssortment
from app.models.stock import Stock

@dataclass
class SellContext:
    requested_qty: float

    product: Product | None = None
    branch: Branch | None = None
    stock: Stock | None = None
    assortment: ProductAssortment | None = None