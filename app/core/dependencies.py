"""Application dependencies for dependency injection."""
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database.session import get_db
from app.services.sub_company import SubCompanyService
from app.services.brand import BrandService
from app.repositories.sub_company import SubCompanyRepository


async def get_sub_company_service(
    session: AsyncSession = Depends(get_db),
) -> SubCompanyService:
    """Get SubCompanyService dependency."""
    return SubCompanyService(session=session)


async def get_brand_service(
    session: AsyncSession = Depends(get_db),
) -> BrandService:
    """Get BrandService dependency with SubCompanyRepository interface injection."""
    sub_company_repo =SubCompanyRepository(session)
    return BrandService(session=session, sub_company_repo=sub_company_repo)
