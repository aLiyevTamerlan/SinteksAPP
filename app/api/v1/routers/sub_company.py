from fastapi import APIRouter, Depends, HTTPException, status

from app.core.dependencies import get_sub_company_service
from app.services.sub_company import SubCompanyService
from app.api.v1.schemas.sub_company import SubCompanyCreate

router = APIRouter()
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_sub_company(
    sub_company_data: SubCompanyCreate,
    service: SubCompanyService = Depends(get_sub_company_service),
):
    """Create a new sub-company."""
    try:
        result = await service.create_sub_company(sub_company_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))