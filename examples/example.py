from __future__ import annotations
import aiosteam
import asyncio


class Example:

    def __init__(self) -> None:
        self.aiosteam = aiosteam.Apply(
            api_key='api_key_here'
        )

    async def task(self):
        steam = await self.aiosteam.custom_to_steamid(
            input('Enter steam account custom URL: ')
        ).process()

        friendlist = await self.aiosteam.get_friendlist(
            steamid=steam.steamid
        ).process()

        print(friendlist)

        await self.aiosteam.close_session()


if __name__ == '__main__': 
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Example().task())
