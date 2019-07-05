from dataclasses import dataclass


@dataclass
class Player:
    steamid: str
    personaname: str
    profileurl: str
    avatar: str
    avatarmedium: str
    avatarfull: str
    personastate: int
    communityvisibilitystate: int
    profilestate: int
    lastlogoff: int
    commentpermission: str
    realname: str = None
    primaryclanid: int = None
    timecreated: int = None
    gameid: int = None
    gameserverip: str = None
    gameextrainfo: str = None
    cityid: int = None
    loccountrycode: str = None
    locstatecode: str = None
    loccityid: int = None
    personastateflags: str = None


@dataclass
class Friend:
    steamid: str
    relationship: str
    friend_since: int


@dataclass
class Achievement:
    apiname: str
    achieved: int
    unlocktime: int


@dataclass
class GameStat:
    name: str
    value: int


@dataclass
class OwnedGame:
    appid: int
    playtime_2weeks: int = None
    playtime_forever: int = None


@dataclass
class RecentlyPlayedGame:
    appid: int
    name: str
    playtime_2weeks: int
    playtime_forever: int
    img_icon_url: str
    img_logo_url: str


@dataclass
class PlayerBans:
    SteamId: str
    CommunityBanned: bool
    VACBanned: bool
    NumberOfVACBans: int
    DaysSinceLastBan: int
    NumberOfGameBans: int
    EconomyBan: bool


@dataclass
class ConvertedURL:
    steamid: str
    success: int
