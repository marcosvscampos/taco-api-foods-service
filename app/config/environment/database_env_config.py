import os
from app.config.environment.env_config import EnvConfig

class DatabaseConfig(EnvConfig):

    def __init__(self):
        self.database = os.environ.get("DB_NAME")
        super().__init__(
            host=os.environ.get("DB_HOST"),
            username=os.environ.get("DB_USERNAME"), 
            password=os.environ.get("DB_PASSWORD")
        )
