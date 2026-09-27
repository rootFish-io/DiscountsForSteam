import httpx
import asyncio

async def update_games():
    logger.info('Update_games')
    url = 'https://www.cheapshark.com/api/1.0/deals'

    async with httpx.AsyncClient(headers={'User-Agent': 'SteamDeals/1.0'}, proxy='http://10.41.123.200:10809') as client:
        response = await client.get(
            url, 
            params={
                'storeID': 1,
                'pageNumber': 0,
                'pageSize': 60
            })
    
        response.raise_for_status()
        total_pages = int(response.headers['X-Total-Page-Count'])
    
        for game in response.json():
            # добавляем нулевую страницу
            pass

        for page in range(1, total_pages + 1):
            response = await client.get(
                url, 
                params={
                    'storeID': 1,
                    'pageNumber': page,
                    'pageSize': 60
                })
            
            response.raise_for_status()

            for game in response.json():
                # добавили в бд остальные страници
                pass
            
            await asyncio.sleep(1)

    logger.info('All games saved')
