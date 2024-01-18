from app.models.food import Food
from app.readers.xslx_reader import read

class FoodService:

    async def load_foods(self):
        status = { 'status' : None }
        
        food = Food()
        reg_count = await food.count()
        if(reg_count > 0):
            print(f"[food_service#load_foods] Database is already loaded with {reg_count} registers")
            status['status'] = f'Database already loaded with {reg_count} registers'
            return status

        table_lines = read()
        for table_item in table_lines:
            food.parse(table_item)
            await food.insert()

        print(f"[food_service#load_foods] All {len(table_lines)} has been load to database")
        status['status'] = 'Completed'
        return status   
              