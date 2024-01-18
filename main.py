import uvicorn

from dotenv import load_dotenv
from app.utils.system import banner

from fastapi import FastAPI

from app.controllers import system_controller
from app.config import database

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await database.init_db()

load_dotenv()

app.include_router(system_controller.router, prefix="/api")
    
def run():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if(__name__ == "__main__"):
    banner()
    run()    