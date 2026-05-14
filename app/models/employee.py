from sqlalchemy import (
    Boolean, Column, Integer, ForeignKey, Date, String
)
from sqlalchemy.orm import relationship

from app.core.database.session import Base

class Position(Base):
    __tablename__ = "Position"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationships
    employee_Position = relationship(
        "EmployeePosition",
        back_populates="position"
    )
 
 
class Employee(Base):
    __tablename__ = "Employees"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationships
    employee_Position = relationship(
        "EmployeePosition",
        back_populates="employee"
    )
 
 
class EmployeePosition(Base):
    __tablename__ = "EmployeePosition"
    
    id = Column(Integer, primary_key=True)
    position_id = Column(Integer, ForeignKey("Position.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("Employees.id"), nullable=False)
    is_active = Column(Boolean, nullable=False)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=True)
    
    # Relationships
    position = relationship("Position", back_populates="employee_Position")
    employee = relationship("Employee", back_populates="employee_Position")

