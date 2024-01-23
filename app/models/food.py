from beanie import Document
from typing import Optional
import uuid

class Food(Document):

    id: Optional[str] = None
    num_food: Optional[int] = None
    name: Optional[str] = None
    calories: Optional[float] = None
    proteins: Optional[float] = None
    fats: Optional[float] = None
    carbohidrates: Optional[float] = None

    class Settings:
        name = "Foods"

    def __str__(self):
        return f"Numero do Alimento - {self.num_food} | Nome - {self.name} | Calorias - {self.calories} | Proteínas - {self.proteins} | Gorduras - {self.fats} | Carboidratos - {self.cabohidrates}"

    def parse(self, item:list):
        self.id = str(uuid.uuid4())
        self.num_food = item[6]
        self.name = item[0]
        self.calories = self.__round(item[1])
        self.proteins = self.__round(item[3])
        self.fats = self.__round(item[4])
        self.carbohidrates = self.__round(item[5])
        return self

    def __round(self, val):
        try:
            return float("{:.2f}".format(val))
        except:    
            return float("0.0")