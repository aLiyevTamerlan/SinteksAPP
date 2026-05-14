"""Application dependencies for dependency injection."""
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database.session import get_db
from app.services.sub_company import SubCompanyService


async def get_sub_company_service(
    session: AsyncSession = Depends(get_db),
) -> SubCompanyService:
    """Get SubCompanyService dependency."""
    return SubCompanyService(session=session)
