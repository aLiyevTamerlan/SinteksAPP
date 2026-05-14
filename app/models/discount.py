from sqlalchemy import (
    Column, Integer, ForeignKey, String, Date, CheckConstraint
)
from sqlalchemy.orm import relationship

from app.core.database.session import Base


class Discount(Base):
    __tablename__ = "Discount"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    percentage = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    priority = Column(
        String(255),
        CheckConstraint("priority IN ('low', 'medium', 'high', 'important')"),
        nullable=False
    )
    
    # Relationships
    discount_branches = relationship("DiscountBranch", back_populates="discount")
    discount_products = relationship("DiscountProduct", back_populates="discount")
    discount_categories = relationship("DiscountCategory", back_populates="discount")
    discount_brands = relationship("DiscountBrand", back_populates="discount")
 
 
class DiscountBranch(Base):
    __tablename__ = "DiscountBranch"
    
    id = Column(Integer, primary_key=True)
    discount_id = Column(Integer, ForeignKey("Discount.id"), nullable=False)
    branch_id = Column(Integer, ForeignKey("Branch.id"), nullable=False)
    
    # Relationships
    discount = relationship("Discount", back_populates="discount_branches")
    branch = relationship("Branch", back_populates="discount_branches")
 
 
class DiscountProduct(Base):
    __tablename__ = "DiscountProduct"
    
    id = Column(Integer, primary_key=True)
    discount_id = Column(Integer, ForeignKey("Discount.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("Product.id"), nullable=False)
    
    # Relationships
    discount = relationship("Discount", back_populates="discount_products")
    product = relationship("Product", back_populates="discount_products")
 
 
class DiscountCategory(Base):
    __tablename__ = "DiscountCategory"
    
    id = Column(Integer, primary_key=True)
    discount_id = Column(Integer, ForeignKey("Discount.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("ProductCategory.id"), nullable=False)
    
    # Relationships
    discount = relationship("Discount", back_populates="discount_categories")
    category = relationship("ProductCategory", back_populates="discount_categories")
 
 
class DiscountBrand(Base):
    __tablename__ = "DiscountBrand"
    
    id = Column(Integer, primary_key=True)
    discount_id = Column(Integer, ForeignKey("Discount.id"), nullable=False)
    brand_id = Column(Integer, ForeignKey("Brand.id"), nullable=False)
    
    # Relationships
    discount = relationship("Discount", back_populates="discount_brands")
    brand = relationship("Brand", back_populates="discount_brands")
 