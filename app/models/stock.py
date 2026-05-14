from sqlalchemy import (
    Column, Integer, ForeignKey
)
from sqlalchemy.orm import relationship

from app.core.database.session import Base

class Stock(Base):
    __tablename__ = "Stock"
    
    id = Column(Integer, primary_key=True)
    branch_id = Column(Integer, ForeignKey("Branch.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("Product.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    
    # Relationships
    branch = relationship("Branch", back_populates="stocks")
    product = relationship("Product", back_populates="stocks")