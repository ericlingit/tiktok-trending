# Tiktok trending videos scraper

Scrape trending video URLs from Tiktok front page, with option to download them.

## Website structure

1. The initial load-in is statically generated with some content preloaded, depending on your screen size.
1. As you scroll further down, the embedded JavaScript calls Tiktok's content API to fetch more videos.

Sample request:

```
GET https://www.tiktok.com/api/recommend/item_list/?aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%29&channel=tiktok_web&cookie_enabled=true&count=30&device_id=7163916748088903169&device_platform=web_pc&focus_state=false&from_page=fyp&history_len=5&is_fullscreen=false&is_page_visible=true&os=linux&priority_region=&referer=&region=TW&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=1080&screen_width=1920&tz_name=Asia%2FTokyo&webcast_language=en&msToken=1dCRzRecIKwoXXt2XNqL659r22i24Rgw-bYYogQujt_fYsxRQDEvUBkmtztQsiWd_OSZUrBvA054t1YNdYSJJxeFtZKaEjDjFjIKMEyesmkprTD-8CLIdIU4TUjrVyPQlntww4jIoWIZ0g==&X-Bogus=DFSzsIVL-isANHNDS0CN4aL1Xb7j&_signature=_02B4Z6wo00001p5YTDQAAIDDDHa3p8mTTUqeWUiAAMUJc3

Host: www.tiktok.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1
DNT: 1
Connection: keep-alive
Cookie: ttwid=1%7CXDWPbqtCdaLFmO1eGUr4uXDfHz1MMPNM6Z80WuPEsb8%7C1667980677%7C488589e2f9e4e8e2b9cbe228dfb34b15c156728ced42d6ea28213599f3ba3381; tt_csrf_token=aHFmhyhT-bSqAzBCPU5omNBjU8AE-xZFTpjI; _abck=46D44C3D862BA83A4923E4D8ED4C9A18~-1~YAAQLuNH0qh7dS+EAQAARzdRWwgFZL/6Efyx+OJ2biRFjNHdM0vWN4zjPA3VxsvPdSHcufgCaMd0QrpUTrcwxxlvvKLQg84ZRYzAzo315nR/De1MzKEj/lapgdWmpRGP5G5Se+tZOKKo4dQQ3jri4biORd9nZNL8CGEeYYBkU4Eaal6W6W2jPB4B4L4eGekN48qQWpaE7ZmCBELa+J5BkAtU43GYG9Yr4m0Xg51cIQUhvVQJIdJN7epjceFXY7yY7WniYnyLgcUyR/hlDpTAvbp7UomUBWHH/CcBpZ4nNVeWdBz+vc6BRA6LTiwDszfkhROrz/WVsmmNXoP/7ql4dO0HWF2Po+L4nJFWb+J3nxk4S2z3NCAn/1FLm/U=~-1~-1~-1; bm_sz=E070FD9E54B63E996E0132C2770C469F~YAAQLuNH0ql7dS+EAQAARzdRWxF8N+H9WFq9WCOm18pHe9q2RKlhqDAfqxQVcuT5u45hOijubQJ01kZU7mQXncajGv20o522eAXqdIdypObDrPGhToNpSdso8C73T+hdCJ1vGPTnEf7Xb2rEO9qDcMBTPBEzWgFQ+QQ+jIf5J+UAV4G81mwbKvWajHRlWBBmEJEVcWgdETwv7epYZQHqrnYwYoN10nJRuNfo4js02fF2eqrsFjVjPtBjkPN991e/bp+UfWu7paacJYDXJA8TSm0kVkonvqfCWPHZ1JZxMercudM=~4602167~4338993; tiktok_webapp_theme=light; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227163916748088903169%22%2C%22timestamp%22:1667979478657}; msToken=1dCRzRecIKwoXXt2XNqL659r22i24Rgw-bYYogQujt_fYsxRQDEvUBkmtztQsiWd_OSZUrBvA054t1YNdYSJJxeFtZKaEjDjFjIKMEyesmkprTD-8CLIdIU4TUjrVyPQlntww4jIoWIZ0g==; msToken=o3S4FYmVVv5QVDZamfIbH6Pc8qQMuXbcChVvvPDk4aMyEnih9jRmsM-JsYQINdry9HimvGLeOjWpKWQehAeUOJr6YCNXvMvZuTbRZ1zMnnAZPPi2U2oU5fCdynb5umJtxjobNtnQfX2rkA==
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Sec-GPC: 1
TE: trailers
```

See `test/response.json` for a full sample response.

Note that all content URLs (images and videos) in the response have a limited life time. They expire after some number of hours.

## tiktok-trending usage guide

Install

```
pip install tiktok-trending
```

Scrape and download

```python
from pathlib import Path

from tiktok_trending import download_video, get_new_posts, parse_response

resp = get_new_posts()
posts = parse_response(resp)
for p in posts:
    vid_name = f"{p.author.uniqueId}_{p.video.id}"
    print(vid_name)
    download_video(
        tik=p,
        out_dir=Path("."),
        filename=vid_name,
        save_metadata=True,
    )
```

## Develop

### Dev env setup

```
git clone https://github.com/ericlingit/tiktok-trending.git
cd tiktok-trending
python3 -m venv venv
source venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt
pip install -e .
pytest
```
