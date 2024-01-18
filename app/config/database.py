from beanie import init_beanie
import motor.motor_asyncio

from app.models.food import Food
from app.config.environment.database_env_config import DatabaseConfig

async def init_db():
    db_config = DatabaseConfig()

    print(f">>> Starting database at Host -> @{db_config.host} - Database -> {db_config.database}")

    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb+srv://{db_config.username}:{db_config.password}@{db_config.host}/{db_config.database}?retryWrites=true&w=majority"
    )

    await init_beanie(database=client.get_database(), document_models=[Food]) 