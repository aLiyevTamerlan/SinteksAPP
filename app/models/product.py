from sqlalchemy import (
    Column, Integer, Numeric, String, Boolean, ForeignKey
)
from sqlalchemy.orm import relationship

from app.core.database.session import Base

class ProductCategory(Base):
    __tablename__ = "ProductCategory"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    
    # Relationships
    products = relationship("Product", back_populates="category")
    discount_categories = relationship("DiscountCategory", back_populates="category")

class ProductAssortment(Base):
    __tablename__ = "ProductAssortment"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    product_id = Column(
        ForeignKey("Product.id"),
        nullable=False
    )

    branch_id = Column(
        ForeignKey("Branch.id"),
        nullable=False
    )
    is_active = Column(Boolean, nullable=False)
    # Relationships
    stocks = relationship("Stock", back_populates="assortment")

class Product(Base):
    __tablename__ = "Product"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey("ProductCategory.id"), nullable=False)
    color = Column(String(255), nullable=False)
    size = Column(Numeric(8, 2), nullable=False)
    purchase_price = Column(Numeric(8, 2), nullable=False)
    base_selling_price = Column(Numeric(8, 2), nullable=False)
    is_active = Column(Boolean, nullable=False)
    
    # Relationships
    category = relationship("ProductCategory", back_populates="products")
    stocks = relationship("Stock", back_populates="product")
    Sale = relationship("Sale", back_populates="product")
    discount_products = relationship("DiscountProduct", back_populates="product")