from fastapi import APIRouter, Depends

from app.dto.food_filter import FoodFilter
from app.dto.food_dto import FoodDTO

from app.services.search_foods_service import SearchFoodsService

router = APIRouter()

@router.get("/", response_model=list[FoodDTO])
async def get_foods_by_filter(params: FoodFilter = Depends()):
    service = SearchFoodsService(params)
    response = await service.execute()
    return response