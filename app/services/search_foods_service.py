from app.models.food import Food
from app.dto.food_filter import FoodFilter
from app.dto.food_dto import FoodDTO

class SearchFoodsService:

    def __init__(self, filters):
        self._food = Food()
        self._filters:FoodFilter = filters
        self._model_filter:dict = self._filters.build_model_filter()

    async def execute(self) -> list[FoodDTO]:
        print(">>> Executing search service")
        print(self._filters)

        foods = await self.__do_search() 
        foods_dto:list[FoodDTO] = []
        for item in foods:
            foods_dto.append(FoodDTO().parse(item))

        return foods_dto
    
    async def __do_search(self):
        return await self._food.find_many(
                self._model_filter['params']
            ).skip(
                self._model_filter['pagination']['start']
            ).limit(
                self._model_filter['pagination']['end']
            ).sort('name').to_list()
        

    
