from sqlalchemy import (
    Column, Integer, String, Boolean
)
from sqlalchemy.orm import relationship

from app.core.database.session import Base


class SubCompany(Base):
    __tablename__ = "SubCompany"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False)

    brand_company_assignments = relationship(
        "BrandCompanyAssignment", 
        back_populates="sub_company",
        foreign_keys="BrandCompanyAssignment.sub_company_id"
    )