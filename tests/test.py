import asyncio
import aiosteam

asteam = aiosteam.Apply(
    api_key='api_key_here'
)

async def task():
    converted = await asteam.custom_to_steamid('test').process()
    request = await asteam.get_friendlist(steamid=converted.steamid).process()
    print(request)
    await asteam.close_session()

loop = asyncio.get_event_loop()
loop.run_until_complete(task())
