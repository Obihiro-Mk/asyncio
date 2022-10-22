
PG_USER = 'postgres'
PG_PASSWORD = 'pass'
PG_HOST = '127.0.0.1'
PG_DB = 'hw_asyncio'
PG_DSN = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:5431/{PG_DB}'
PG_DSN_ALC = f'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:5431/{PG_DB}'