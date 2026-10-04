from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import asyncio

import database
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

app.add_middleware(
	CORSMiddleware,
	allow_origins=[
		"http://localhost:5173",
		"http://127.0.0.1:5173",
	],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get('/games')
async def root(
	search: str | None = None,
	page: int = Query(1, ge=1), 
	limit: int = Query(60, ge=1, le=60)
):
	async with database.pool.acquire() as conn:
		games_record = await conn.fetch(
			'''
			SELECT 
				steam_app_id,
				name, 
				price, 
				discounted_price,
				updated_at,
                url,
                discount_percent,
                steam_rating_percent
			FROM games
			ORDER BY discount_percent
			LIMIT $1
			OFFSET $2
			''',
			limit,
			(page - 1) * limit
		)

		total = await conn.fetch('SELECT COUNT(*) FROM games')

	games = [dict(record) for record in games_record]

	return {
		'games': games, 
		'page': page, 
		'limit': limit,
		'total': total[0]['count']
	}