from app.models.food import Food
from app.readers.xslx_reader import read

from app.executors.food_thread_executor import FoodThreadExecutor

class FoodService:
    
    def __init__(self):
        self._food = Food()
        self._executor = FoodThreadExecutor(model=self._food)

    async def load_foods(self):
        status = {}
        
        reg_count = await self._food.count()
        if(reg_count > 0):
            print(f"[food_service#load_foods] Database is already loaded with {reg_count} registers")
            status['status'] = f'Database already loaded with {reg_count} registers'
            return status

        table_lines = read()
        self._executor.execute(items=table_lines)
            
        print(f"[food_service#load_foods] All {len(table_lines)} has been load to database")
        status['status'] = 'Completed'
        return status           