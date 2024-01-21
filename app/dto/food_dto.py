from pydantic import BaseModel
from app.models.food import Food

class FoodDTO(BaseModel):

    id:str = None
    num_food:int = None
    name:str = None
    calories:float = None
    proteins:float = None
    fats:float = None
    carbohidrates:float = None

    def parse(self, model:Food):
        self.id=model.id
        self.num_food=model.num_food
        self.name=model.name
        self.calories=model.calories
        self.proteins=model.proteins
        self.fats=model.fats
        self.carbohidrates=model.carbohidrates
        return self

