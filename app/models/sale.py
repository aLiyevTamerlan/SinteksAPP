from sqlalchemy import (
    Column, Integer, Date, ForeignKey
)
from sqlalchemy.orm import relationship

from app.core.database.session import Base


class Sale(Base):
    __tablename__ = "Sale"
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("Product.id"), nullable=False)
    branch_id = Column(Integer, ForeignKey("Branch.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    sale_time = Column(Date, nullable=False)
    discounted_selling_price = Column(Integer, nullable=False)
    discount_percentage = Column(Integer, nullable=False)
    seller_id = Column(Integer, ForeignKey("Employees.id"),nullable=False)
    
    # Relationships
    product = relationship("Product", back_populates="Sale")
    branch = relationship("Branch", back_populates="Sale")