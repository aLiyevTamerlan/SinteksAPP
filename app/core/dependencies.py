"""Application dependencies for dependency injection."""
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database.session import get_db
from app.services.sub_company import SubCompanyService
from app.services.brand import BrandService
from app.services.branch import BranchService
from app.services.product import ProductService
from app.services.assortment import AssortmentService
from app.services.stock import StockService


async def get_sub_company_service(
    session: AsyncSession = Depends(get_db),
) -> SubCompanyService:
    """Get SubCompanyService dependency."""
    return SubCompanyService(session=session)


async def get_brand_service(
    session: AsyncSession = Depends(get_db),
    sub_company_service: SubCompanyService = Depends(get_sub_company_service),
) -> BrandService:
    """Get BrandService dependency with SubCompanyService injection."""
    return BrandService(session=session, sub_company_service=sub_company_service)


async def get_branch_service(
    session: AsyncSession = Depends(get_db),
    brand_service: BrandService = Depends(get_brand_service),
) -> BranchService:
    """Get BranchService dependency with BrandService injection."""
    return BranchService(session=session, brand_service=brand_service)


async def get_assortment_service(
    session: AsyncSession = Depends(get_db),
) -> AssortmentService:
    """Get AssortmentService dependency."""
    return AssortmentService(session=session)


async def get_stock_service(
    session: AsyncSession = Depends(get_db),
) -> StockService:
    """Get StockService dependency."""
    return StockService(session=session)


async def get_product_service(
    session: AsyncSession = Depends(get_db),
    brand_service: BrandService = Depends(get_brand_service),
    branch_service: BranchService = Depends(get_branch_service),
    assortment_service: AssortmentService = Depends(get_assortment_service),
    stock_service: StockService = Depends(get_stock_service),
) -> ProductService:
    """Get ProductService dependency with service injection."""
    return ProductService(
        session=session,
        brand_service=brand_service,
        branch_service=branch_service,
        assortment_service=assortment_service,
        stock_service=stock_service,
    )
