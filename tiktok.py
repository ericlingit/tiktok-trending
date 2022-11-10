import json
from dataclasses import dataclass, asdict


@dataclass
class Author:
    avatarLarger: str
    avatarMedium: str
    avatarThumb: str
    commentSetting: int
    downloadSetting: int
    duetSetting: int
    ftc: bool
    id: str
    isADVirtual: str
    nickname: str
    openFavorite: bool
    privateAccount: bool
    relation: int
    secUid: str
    secret: bool
    signature: str
    stitchSetting: int
    ttSeller: bool
    uniqueId: str
    url: str
    verified: bool


@dataclass
class AuthorStats:
    diggCount: int
    followerCount: int
    followingCount: int
    heart: int
    heartCount: int
    videoCount: int


@dataclass
class Music:
    album: str
    authorName: str
    coverLarge: str
    coverMedium: str
    coverThumb: str
    duration: int
    id: str
    original: bool
    playUrl: str
    title: str


@dataclass
class Video:
    bitrate: int
    codecType: str
    cover: str
    definition: str
    downloadAddr: str
    duration: int
    dynamicCover: str
    encodeUserTag: str
    encodedType: str
    format: str
    height: int
    id: str
    originCover: str
    playAddr: str
    ratio: str
    reflowCover: str
    videoQuality: str
    width: int


@dataclass
class Stats:
    commentCount: int
    diggCount: int
    playCount: int
    shareCount: int


@dataclass
class Tik:
    author: Author
    createTime: int
    desc: str
    id: str
    isAd: bool
    music: Music
    stats: Stats
    url: str
    video: Video


if __name__ == "__main__":
    with open("sample-response.json") as fh:
        data: dict = json.load(fh)
        i = data.get("itemList", [{}])[0]

        # Author.
        a = i.get("author", {})
        author = Author(**a, url=f"https://www.tiktok.com/@{a.get('id', '')}")

        # Author stats.
        ax = i.get("authorStats", {})
        author_stats = AuthorStats(**ax)

        # Music.
        mu = i.get("music", {})
        music = Music(**mu)

        # Stats.
        st = i.get("stats", {})
        stats = Stats(**st)

        # Video.
        v = i.get("video", {})
        v.pop("bitrateInfo")
        v.pop("shareCover")
        v.pop("volumeInfo")
        v.pop("zoomCover")
        video = Video(**v)

    item = Tik(
        author=author,
        createTime=i.get("createTime", -1),
        desc=i.get("desc", ""),
        id=i.get("id", ""),
        isAd=i.get("isAd", False),
        music=music,
        stats=stats,
        video=video,
        url=f"https://www.tiktok.com/@{author.id}/video/{video.id}",
    )

    from pprint import pprint

    pprint(asdict(item))
