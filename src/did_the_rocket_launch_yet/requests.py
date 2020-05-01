import aiohttp

from src.did_the_rocket_launch_yet.utils.urls_rocket import get_url_rocket


async def get_video_info():
    async with aiohttp.ClientSession() as session:
        async with session.get(get_url_rocket()) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                return None
