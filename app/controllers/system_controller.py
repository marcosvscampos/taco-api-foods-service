from fastapi import APIRouter

from app.services.load_foods_service import LoadFoodsService


router = APIRouter()

@router.post("/sync/foods")
async def sync_foods():
    service = LoadFoodsService()
    response = await service.execute()
    return response