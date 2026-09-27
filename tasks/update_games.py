import httpx
import asyncio
import database
from datetime import datetime, timezone

PROXY = 'http://10.41.123.200:10809' # это только для меня
BASE_URL = 'https://www.cheapshark.com/api/1.0/deals'
PAGE_SIZE = 60
STORE_ID = 1 # Steam


async def insert_page(conn, games):
    for game in games:
        if game['steamAppID'] is None:
            print(f'skip {game["title"]} - no steamAppID')
            continue

        print(game['title'], '-', game['steamAppID'])
        await conn.execute(
            '''
            INSERT INTO games (
                steam_app_id,
                name,
                price,
                discounted_price,
                updated_at
            )
            VALUES ($1, $2, $3, $4, NOW())

            ON CONFLICT (steam_app_id)
            DO UPDATE SET
                name = EXCLUDED.name,
                price = EXCLUDED.price,
                discounted_price = EXCLUDED.discounted_price,
                updated_at = NOW()
            ''',
            int(game['steamAppID']),
            game['title'],
            game['normalPrice'],
            game['salePrice']
        )


async def get_page(client, pageNumber):
    response = await client.get(
        BASE_URL, 
        params={'storeID': STORE_ID, 'pageNumber': pageNumber, 'pageSize': PAGE_SIZE}
    )
    
    response.raise_for_status()
    print(pageNumber)
    return response


async def update_games():
    print('update_games')
    started_at = datetime.now(timezone.utc)

    async with httpx.AsyncClient(headers={'User-Agent': 'SteamDeals/1.0'}, proxy=PROXY, timeout=30) as client:
        response = await get_page(client, 0)
        total_pages = int(response.headers['X-Total-Page-Count'])

        async with database.pool.acquire() as conn:
            await insert_page(conn, response.json())
               
            for page in range(1, total_pages + 1):
                response = await get_page(client, page)
                await insert_page(conn, response.json())
                await asyncio.sleep(1)

            await conn.execute(
                'DELETE FROM games WHERE updated_at < $1',
                started_at
            )
