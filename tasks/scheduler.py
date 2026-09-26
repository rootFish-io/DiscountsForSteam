import asyncio
from tasks.update_games import update_games

async def scheduler():
    while True:
        await update_games()
        await asyncio.sleep(60 * 60)

