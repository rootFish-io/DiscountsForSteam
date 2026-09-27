import asyncpg

pool: asyncpg.Pool | None = None


async def connect_db():
    global pool

    pool = await asyncpg.create_pool(
        user='postgres',
        database='postgres',
        password='1234567890',
        host='localhost',
        port=5432
    )

async def close_db():
    global pool

    if pool:
        await pool.close()
