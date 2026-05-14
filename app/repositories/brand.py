from datetime import datetime, timezone

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.brand import Brand, BrandCompanyAssignment


class BrandRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, brand_data: dict) -> Brand:
        """Create a new brand."""
        stmt = insert(Brand).values(**brand_data).returning(Brand)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()
    
    async def reassign_company(self, brand_id: int, new_sub_company_id: int) -> Brand:
        """Change brand's company (handles the history internally)."""
        # Deactivate old assignment
        await self.session.execute(
            update(BrandCompanyAssignment)
            .where(
                (BrandCompanyAssignment.brand_id == brand_id) &
                (BrandCompanyAssignment.is_active == True)
            )
            .values(is_active=False, deactivated_at=datetime.now(timezone.utc))
        )
        await self.session.execute(
            insert(BrandCompanyAssignment).values(
                brand_id=brand_id,
                sub_company_id=new_sub_company_id,
                is_active=True,
                created_at=datetime.now(timezone.utc)
            )
        )
        
        await self.session.commit()
