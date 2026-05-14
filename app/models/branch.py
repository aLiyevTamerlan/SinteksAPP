from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey
)
from sqlalchemy.orm import relationship

from app.core.database.session import Base

class Branch(Base):
    __tablename__ = "Branch"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    brand_id = Column(Integer, ForeignKey("Brand.id"), nullable=False)
    address = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False)
    
    # Relationships
    brand = relationship("Brand", back_populates="branches")
    stocks = relationship("Stock", back_populates="branch")
    Sale = relationship("Sale", back_populates="branch")
    discount_branches = relationship("DiscountBranch", back_populates="branch")