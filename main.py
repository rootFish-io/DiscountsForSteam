from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

import asyncio
import database
import httpx

from tasks.scheduler import scheduler
from database import connect_db, close_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(scheduler())
    await connect_db()

    yield

    task.cancel()
    await close_db()


app = FastAPI(lifespan=lifespan)


@app.get('/')
async def root():
    return {'work': True}
