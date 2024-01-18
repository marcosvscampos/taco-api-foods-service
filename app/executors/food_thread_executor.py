import asyncio
from concurrent.futures import ThreadPoolExecutor

from app.models.food import Food

class FoodThreadExecutor:

    def __init__(self, model:Food):
        self._model = model

    # Separa a ação de salvar o alimento no banco de dados 
    # como uma task para ser executada em paralelo
    async def _task(self, item):
        self._model.parse(item)
        await self._model.insert()  

    # Essa função serve para encapsular a task acima para ser executada 
    def _thread_wrapper(self, task):
        asyncio.run(task)

    def execute(self, items):
        with ThreadPoolExecutor(max_workers=4) as executor:
            # 1 - Crie uma lista de tasks a serem executadas usando uma lista
            # Aqui estou criando uma task para cada linha em "items" que são as
            # linhas lidas no XSLX para salvar os dados em paralelo
            tasks = [self._task(item) for item in items]
            # 2 - Use o executor.map com o encapsulante thread_wrapper()
            # Esse encapsulante é necessário pois a função de 
            # salvar dados no MongoDB é assincrona e precisa ser rodada em outra rotina 
            executor.map(self._thread_wrapper, tasks)
            # 3 - Insira o shutdown como True para dizer para o programa aguardar todas as tasks
            # completarem para dar procedimento
            executor.shutdown(wait=True)