from fastapi import FastAPI, HTTPException, Query
from contextlib import asynccontextmanager

import asyncio
import database
import httpx

from tasks.scheduler import scheduler
from database import connect_db, close_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    #task = asyncio.create_task(scheduler())
    await connect_db()

    yield

    #task.cancel()
    await close_db()


app = FastAPI(lifespan=lifespan)


@app.get('/games')
async def root(
    search: str | None = None,
    page: int = Query(1, ge=1), 
    limit: int = Query(60, ge=1, le=60)
):
    async with database.pool.acquire() as conn:
        games_record = await conn.fetch(
            '''
            SELECT steam_app_id, name, price, discounted_price FROM games
            ORDER BY name
            LIMIT $1
            OFFSET $2
            ''',
            limit,
            (page - 1) * limit
        )

    games = [dict(record) for record in games_record]

    return games
