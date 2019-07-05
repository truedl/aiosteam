from __future__ import annotations
from typing import Union
from .struct import *
import aiohttp


class Get:

    def __init__(self, main) -> None:
        self.main = main
        self.session = aiohttp.ClientSession()

        self.request_types = {
            'get_player': Player,
            'get_player_bans': PlayerBans,
            'vanityurl_to_steamid': ConvertedURL,
            'get_friendlist': Friend,
            'get_achievements': Achievement,
            'get_game_user_stats': GameStat,
            'get_owned_games': OwnedGame,
            'get_recently_played': RecentlyPlayedGame
        }

        self.request_key = {
            'get_player': ['response', 'players'],
            'get_friendlist': ['friendslist', 'friends'],
            'get_achievements': ['playerstats', 'achievements'],
            'get_game_user_stats': ['playerstats', 'stats'],
            'get_owned_games': ['response', 'games'],
            'get_recently_played': ['response', 'games'],
            'get_player_bans': ['players'],
            'vanityurl_to_steamid': ['response']
        }

        self.special_process = {
            'get_friendlist': self.special_loop_process,
            'get_achievements': self.special_loop_process,
            'get_game_user_stats': self.special_loop_process,
            'get_owned_games': self.special_loop_process,
            'get_recently_played': self.special_loop_process
        }

    async def process(self) -> Union[ConvertedURL, PlayerBans, Player, list]:
        request_url = f'{self.main.base_url}{self.main.endpoint}'

        async with self.session.get(request_url) as resp:

            resp = await resp.json()
            request_key = self.request_key[self.main.request]
            resp_fetch = resp
            for key in request_key:
                resp_fetch = resp_fetch[key]

            if self.main.request not in self.special_process:
                try:
                    resp_fetch = resp_fetch[0]
                except:
                    pass

                request_class = self.request_types[self.main.request]

                return request_class(**resp_fetch)

            else:
                return self.special_process[self.main.request](resp_fetch, self.main.request)

    def special_loop_process(self, to_list: list, request_type: str) -> list:
        return_list = []

        for dict_obj in to_list:
            return_list.append(self.request_types[request_type](**dict_obj))

        return return_list
