from fastapi import APIRouter

from app.services.food_service import FoodService

router = APIRouter()

@router.get("/system/sync/foods")
async def sync_foods():
    service = FoodService()
    response = await service.load_foods()
    return response