import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

import requests


@dataclass
class AuthorStats:
    diggCount: int
    followerCount: int
    followingCount: int
    heart: int
    heartCount: int
    videoCount: int


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
    stats: AuthorStats
    stitchSetting: int
    ttSeller: bool
    uniqueId: str
    url: str
    verified: bool


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
class Stats:
    commentCount: int
    diggCount: int
    playCount: int
    shareCount: int


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


request_url = "https://www.tiktok.com/api/recommend/item_list/?aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%29&channel=tiktok_web&cookie_enabled=true&count=30&device_id=7163916748088903169&device_platform=web_pc&focus_state=false&from_page=fyp&history_len=5&is_fullscreen=false&is_page_visible=true&os=linux&priority_region=&referer=&region=TW&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=1080&screen_width=1920&tz_name=Asia%2FTokyo&webcast_language=en&msToken=1dCRzRecIKwoXXt2XNqL659r22i24Rgw-bYYogQujt_fYsxRQDEvUBkmtztQsiWd_OSZUrBvA054t1YNdYSJJxeFtZKaEjDjFjIKMEyesmkprTD-8CLIdIU4TUjrVyPQlntww4jIoWIZ0g==&X-Bogus=DFSzsIVL-isANHNDS0CN4aL1Xb7j&_signature=_02B4Z6wo00001p5YTDQAAIDDDHa3p8mTTUqeWUiAAMUJc3"
request_headers = {
    "Host": "www.tiktok.com",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": "ttwid=1%7CXDWPbqtCdaLFmO1eGUr4uXDfHz1MMPNM6Z80WuPEsb8%7C1667980677%7C488589e2f9e4e8e2b9cbe228dfb34b15c156728ced42d6ea28213599f3ba3381; tt_csrf_token=aHFmhyhT-bSqAzBCPU5omNBjU8AE-xZFTpjI; _abck=46D44C3D862BA83A4923E4D8ED4C9A18~-1~YAAQLuNH0qh7dS+EAQAARzdRWwgFZL/6Efyx+OJ2biRFjNHdM0vWN4zjPA3VxsvPdSHcufgCaMd0QrpUTrcwxxlvvKLQg84ZRYzAzo315nR/De1MzKEj/lapgdWmpRGP5G5Se+tZOKKo4dQQ3jri4biORd9nZNL8CGEeYYBkU4Eaal6W6W2jPB4B4L4eGekN48qQWpaE7ZmCBELa+J5BkAtU43GYG9Yr4m0Xg51cIQUhvVQJIdJN7epjceFXY7yY7WniYnyLgcUyR/hlDpTAvbp7UomUBWHH/CcBpZ4nNVeWdBz+vc6BRA6LTiwDszfkhROrz/WVsmmNXoP/7ql4dO0HWF2Po+L4nJFWb+J3nxk4S2z3NCAn/1FLm/U=~-1~-1~-1; bm_sz=E070FD9E54B63E996E0132C2770C469F~YAAQLuNH0ql7dS+EAQAARzdRWxF8N+H9WFq9WCOm18pHe9q2RKlhqDAfqxQVcuT5u45hOijubQJ01kZU7mQXncajGv20o522eAXqdIdypObDrPGhToNpSdso8C73T+hdCJ1vGPTnEf7Xb2rEO9qDcMBTPBEzWgFQ+QQ+jIf5J+UAV4G81mwbKvWajHRlWBBmEJEVcWgdETwv7epYZQHqrnYwYoN10nJRuNfo4js02fF2eqrsFjVjPtBjkPN991e/bp+UfWu7paacJYDXJA8TSm0kVkonvqfCWPHZ1JZxMercudM=~4602167~4338993; tiktok_webapp_theme=light; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227163916748088903169%22%2C%22timestamp%22:1667979478657}; msToken=1dCRzRecIKwoXXt2XNqL659r22i24Rgw-bYYogQujt_fYsxRQDEvUBkmtztQsiWd_OSZUrBvA054t1YNdYSJJxeFtZKaEjDjFjIKMEyesmkprTD-8CLIdIU4TUjrVyPQlntww4jIoWIZ0g==; msToken=o3S4FYmVVv5QVDZamfIbH6Pc8qQMuXbcChVvvPDk4aMyEnih9jRmsM-JsYQINdry9HimvGLeOjWpKWQehAeUOJr6YCNXvMvZuTbRZ1zMnnAZPPi2U2oU5fCdynb5umJtxjobNtnQfX2rkA==",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "TE": "trailers",
}


def get_new_posts() -> dict:
    """Call Tiktok's content API, and return the raw JSON response."""
    resp = requests.get(url=request_url, headers=request_headers)
    resp.raise_for_status()
    return resp.json()


def parse_item(item: dict) -> Tik:
    """Parse one `item` and return a Tik object."""
    # Author stats.
    ax = item.get("authorStats", {})
    author_stats = AuthorStats(
        diggCount=ax.get("diggCount", 0),
        followerCount=ax.get("followerCount", 0),
        followingCount=ax.get("followingCount", 0),
        heart=ax.get("heart", 0),
        heartCount=ax.get("heartCount", 0),
        videoCount=ax.get("videoCount", 0),
    )

    # Author.
    a = item.get("author", {})
    if "roomId" in a:
        a.pop("roomId")
    author = Author(
        avatarLarger=a.get("avatarLarger", ""),
        avatarMedium=a.get("avatarMedium", ""),
        avatarThumb=a.get("avatarThumb", ""),
        commentSetting=a.get("commentSetting", 0),
        downloadSetting=a.get("downloadSetting", 0),
        duetSetting=a.get("duetSetting", 0),
        ftc=a.get("ftc", False),
        id=a.get("id", ""),
        isADVirtual=a.get("isADVirtual", ""),
        nickname=a.get("nickname", ""),
        openFavorite=a.get("openFavorite", False),
        privateAccount=a.get("privateAccount", False),
        relation=a.get("relation", 0),
        secUid=a.get("secUid", ""),
        secret=a.get("secret", False),
        signature=a.get("signature", ""),
        stats=author_stats,
        stitchSetting=a.get("stitchSetting", 0),
        ttSeller=a.get("ttSeller", False),
        uniqueId=a.get("uniqueId", ""),
        url=f"https://www.tiktok.com/@{a.get('uniqueId', '')}",
        verified=a.get("verified", False),
    )

    # Music.
    mu = item.get("music", {})
    music = Music(
        album=mu.get("album", ""),
        authorName=mu.get("authorName", ""),
        coverLarge=mu.get("coverLarge", ""),
        coverMedium=mu.get("coverMedium", ""),
        coverThumb=mu.get("coverThumb", ""),
        duration=mu.get("duration", 0),
        id=mu.get("id", ""),
        original=mu.get("original", False),
        playUrl=mu.get("playUrl", ""),
        title=mu.get("title", ""),
    )

    # Stats.
    st = item.get("stats", {})
    stats = Stats(
        commentCount=st.get("commentCount", 0),
        diggCount=st.get("diggCount", 0),
        playCount=st.get("playCount", 0),
        shareCount=st.get("shareCount", 0),
    )

    # Video.
    v = item.get("video", {})
    video = Video(
        bitrate=v.get("bitrate", 0),
        codecType=v.get("codecType", ""),
        cover=v.get("cover", ""),
        definition=v.get("definition", ""),
        downloadAddr=v.get("downloadAddr", ""),
        duration=v.get("duration", 0),
        dynamicCover=v.get("dynamicCover", ""),
        encodeUserTag=v.get("encodeUserTag", ""),
        encodedType=v.get("encodedType", ""),
        format=v.get("format", ""),
        height=v.get("height", 0),
        id=v.get("id", ""),
        originCover=v.get("originCover", ""),
        playAddr=v.get("playAddr", ""),
        ratio=v.get("ratio", ""),
        reflowCover=v.get("reflowCover", ""),
        videoQuality=v.get("videoQuality", ""),
        width=v.get("width", 0),
    )

    return Tik(
        author=author,
        createTime=item.get("createTime", 0),
        desc=item.get("desc", ""),
        id=item.get("id", ""),
        isAd=item.get("isAd", False),
        music=music,
        stats=stats,
        video=video,
        url=f"https://www.tiktok.com/@{author.uniqueId}/video/{video.id}",
    )


def parse_response(response_json: dict) -> List[Tik]:
    """Parse raw JSON response returned by Tiktok's content API."""
    items = response_json.get("itemList", {})
    return [parse_item(item) for item in items]


def download_video(tik: Tik, out_dir: Path, filename: str, save_metadata: bool) -> None:
    """Download the video in `tik`, and save it as `filename` in `out_dir`.
    File extension (like .mp4) will be automatically added for you.
    If `save_metadata` is True, `tik` will be serialized to a JSON file and
    saved alongside the video.
    """
    resp = requests.get(tik.video.downloadAddr, request_headers, stream=True)
    resp.raise_for_status()

    with (out_dir / f"{filename}.{tik.video.format}").open("wb") as fh:
        for chunk in resp.iter_content(2**14):  # Read 16 KibiBytes at a time.
            fh.write(chunk)

    if save_metadata:
        with (out_dir / f"{filename}.json").open("w") as fh:
            json.dump(asdict(tik), fh, ensure_ascii=False, indent=4)
