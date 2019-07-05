import asyncio
import aiosteam

asteam = aiosteam.Apply(
    api_key='api_key_here'
)

async def task():
    request = asteam.custom_to_steamid('test')
    resp = await request.process()
    print(resp)
    await asteam.close_session()

loop = asyncio.get_event_loop()
loop.run_until_complete(task())
