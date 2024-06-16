from config.database import DatabaseConfig

database_config = DatabaseConfig()

engine = database_config.get_engine()

async_session_maker = database_config.get_session()

async def get_async_session():
    async with async_session_maker() as session:
        yield session