from fastapi import Query
from typing import Optional
from pydantic import BaseModel

class FoodFilter(BaseModel):

    name: Optional[str] = Query(None, description='Parte do nome do alimento')
    page: int = Query(1, ge=1, description='Número da página')
    size: int = Query(10, ge=1, le=100, description='Limite de registros por página')

    def build_model_filter(self) -> dict:
        filter = {
            'params': {},
            'pagination': {}
        }
        
        if(self.name):
            filter['params']['name'] = {'$regex': f".*{self.name}.*", '$options': "i"}

        filter['pagination']['start'] = (self.page - 1) * self.size
        filter['pagination']['end'] = filter['pagination']['start'] + self.size
        
        return filter     