from __future__ import annotations
from .process import Get
import aiohttp


class Apply:

    base_url = 'http://api.steampowered.com/'

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.get = Get(self)

    async def close_session(self) -> None:
        await self.get.session.close()

    def get_player(self, steamid: str) -> Get:
        self.endpoint = f'ISteamUser/GetPlayerSummaries/v0002/?key={self.api_key}&steamids={steamid}'
        self.request = 'get_player'
        return self.get

    def get_friendlist(self, steamid: str) -> Get:
        self.endpoint = f'ISteamUser/GetFriendList/v0001/?key={self.api_key}&steamid={steamid}&relationship=friend'
        self.request = 'get_friendlist'
        return self.get

    def get_achievements(self, steamid: str, appid: str) -> Get:
        self.endpoint = f'ISteamUserStats/GetPlayerAchievements/v0001/?appid={appid}&key={self.api_key}&steamid={steamid}'
        self.request = 'get_achievements'
        return self.get

    def get_game_user_stats(self, steamid: str, appid: str) -> Get:
        self.endpoint = f'ISteamUserStats/GetUserStatsForGame/v0002/?appid={appid}&key={self.api_key}&steamid={steamid}'
        self.request = 'get_game_user_stats'
        return self.get

    def get_owned_games(self, steamid: str) -> Get:
        self.endpoint = f'IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={steamid}'
        self.request = 'get_owned_games'
        return self.get

    def get_recently_played_games(self, steamid: str) -> Get:
        self.endpoint = f'IPlayerService/GetRecentlyPlayedGames/v0001/?key={self.api_key}&steamid={steamid}'
        self.request = 'get_recently_played'
        return self.get

    def get_player_bans(self, steamid: str) -> Get:
        self.endpoint = f'ISteamUser/GetPlayerBans/v1/?key={self.api_key}&steamids={steamid}'
        self.request = 'get_player_bans'
        return self.get

    def convert_vanityurl_to_steamid(self, vanity_url: str) -> Get:
        self.endpoint = f'ISteamUser/ResolveVanityURL/v0001/?key={self.api_key}&vanityurl={vanity_url}'
        self.request = 'vanityurl_to_steamid'
        return self.get

    @property
    def custom_to_steamid(self) -> Get:
        return self.convert_vanityurl_to_steamid
