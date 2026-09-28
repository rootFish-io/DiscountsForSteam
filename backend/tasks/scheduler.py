import asyncio
from tasks.update_games import update_games

async def scheduler():
    try:
        while True:
            await update_games()
            await asyncio.sleep(3600)

    except Exception:
        import traceback
        traceback.print_exc()
        raise

