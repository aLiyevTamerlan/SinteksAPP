from sqlalchemy import (
    Column, DateTime, Integer, String, Boolean, ForeignKey
)
from sqlalchemy.orm import relationship

from app.core.database.session import Base

class Brand(Base):
    __tablename__ = "Brand"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False)
    
    # Relationships
    branches = relationship("Branch", back_populates="brand")
    brand_company_assignments = relationship(
        "BrandCompanyAssignment", 
        back_populates="brand"
    )
    discount_brands = relationship("DiscountBrand", back_populates="brand")

class BrandCompanyAssignment(Base):
    __tablename__ = "BrandCompanyAssignment"
    
    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey("Brand.id"), nullable=False)
    sub_company_id = Column(Integer, ForeignKey("SubCompany.id"), nullable=False)
    deactivated_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, nullable=False)
    
    # Relationships
    brand = relationship("Brand", back_populates="brand_company_assignments")
    sub_company = relationship("SubCompany", back_populates="brand_company_assignments")