# Tiktok scraper

Scrape tiktok front page videos URLs.

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

Sample response (JSON, truncated. See `sample-response.json` for full response).

Note that all content URLs (images and videos) in the response have a limited life time. They expire after some number of hours.

```json
{
    "extra": {
        "fatal_item_ids": [],
        "logid": "2022110908402001024501106913087F41",
        "now": 1667983221000
    },
    "hasMore": true,
    "itemList": [ // 26 items in total
        {
            "adAuthorization": false,
            "adLabelVersion": 0,
            "author": {
                "avatarLarger": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-avt-0068-giso/4b15546d4ae3567a00596a5c8cbdf92d~c5_1080x1080.jpeg?x-expires=1668153600\u0026x-signature=4g224Pf4sHp1I82mb0911Jj84ew%3D",
                "avatarMedium": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-avt-0068-giso/4b15546d4ae3567a00596a5c8cbdf92d~c5_720x720.jpeg?x-expires=1668153600\u0026x-signature=OLI7yFDprVLfFeNrM41ysbSrx4w%3D",
                "avatarThumb": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-avt-0068-giso/4b15546d4ae3567a00596a5c8cbdf92d~c5_100x100.jpeg?x-expires=1668153600\u0026x-signature=hP2plJ4a2yiWNJDaprskN9qvEyk%3D",
                "commentSetting": 0,
                "downloadSetting": 0,
                "duetSetting": 1,
                "ftc": false,
                "id": "62735666087",
                "isADVirtual": false,
                "nickname": "𝑳𝒂𝒍𝒂",
                "openFavorite": false,
                "privateAccount": false,
                "relation": 0,
                "secUid": "MS4wLjABAAAAT7vXNpQ88EBENnzPiUbCvQhACymPVlNaPUepCW89xXY",
                "secret": false,
                "signature": "Ins:lala._.0412 \nYoutube: 菈菈Lala\n2004.4.12（18y)",
                "stitchSetting": 1,
                "ttSeller": false,
                "uniqueId": "lala._.0412",
                "verified": true
            },
            "authorStats": {
                "diggCount": 15400,
                "followerCount": 829000,
                "followingCount": 24,
                "heart": 31500000,
                "heartCount": 31500000,
                "videoCount": 317
            },
            "createTime": 1667019452,
            "desc": "末班車還來得及嗎🥹",
            "digged": false,
            "duetDisplay": 0,
            "duetEnabled": false,
            "duetInfo": {
                "duetFromId": "0"
            },
            "effectStickers": [
                {
                    "ID": "1805988",
                    "name": "細閃果凍妝",
                    "stickerStats": {
                        "useCount": 0
                    }
                }
            ],
            "forFriend": false,
            "id": "7159794001544056091",
            "isAd": false,
            "itemCommentStatus": 0,
            "itemMute": false,
            "music": {
                "album": "",
                "authorName": "沙發馬鈴薯¹⁴",
                "coverLarge": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-avt-0068-giso/ddbaebe7cb7a9c18baa66f7e0f410d16~c5_1080x1080.jpeg?x-expires=1668153600\u0026x-signature=cF23qzlMGiTG8vmvwvaey5JAdm4%3D",
                "coverMedium": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-avt-0068-giso/ddbaebe7cb7a9c18baa66f7e0f410d16~c5_720x720.jpeg?x-expires=1668153600\u0026x-signature=Xltee6s%2FwoZtk7jPeevKkbcjqqU%3D",
                "coverThumb": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-avt-0068-giso/ddbaebe7cb7a9c18baa66f7e0f410d16~c5_100x100.jpeg?x-expires=1668153600\u0026x-signature=NCmr9f%2BVyTguu6Tb9r6VyXyXokk%3D",
                "duration": 13,
                "id": "7152061788027112218",
                "original": true,
                "playUrl": "https://sf16-ies-music.tiktokcdn.com/obj/ies-music-aiso/7152068372321078042.mp3",
                "title": "风夜行 DJ版"
            },
            "officalItem": false,
            "originalItem": false,
            "privateItem": false,
            "secret": false,
            "shareEnabled": true,
            "showNotPass": false,
            "stats": {
                "commentCount": 406,
                "diggCount": 134800,
                "playCount": 961400,
                "shareCount": 873
            },
            "stitchDisplay": 0,
            "stitchEnabled": true,
            "video": {
                "bitrate": 2114595,
                "bitrateInfo": [
                    {
                        "Bitrate": 2114595,
                        "CodecType": "h264",
                        "GearName": "normal_720_0",
                        "PlayAddr": {
                            "DataSize": 3541155,
                            "FileCs": "c:0-15812-b84b",
                            "FileHash": "4efa016d2213e0d2a94d37f9f21f9adb",
                            "Uri": "v0f025gc0000cdeb5d3c77u931v3qvbg",
                            "UrlKey": "v0f025gc0000cdeb5d3c77u931v3qvbg_h264_720p_2114595",
                            "UrlList": [
                                "https://v16-webapp.tiktok.com/29cab804f5e93ac94964d941c424a7f8/636bbbe1/video/tos/useast2a/tos-useast2a-pve-0037-aiso/8abe21a3ddfa49fba5f86bd9a4333f2d/?a=1988\u0026ch=0\u0026cr=0\u0026dr=0\u0026lr=tiktok\u0026cd=0%7C0%7C1%7C0\u0026cv=1\u0026br=4130\u0026bt=2065\u0026cs=0\u0026ds=3\u0026ft=_GC~MBMyq8Z48IYhe2NM4Qml7GbRyu8\u0026mime_type=video_mp4\u0026qs=0\u0026rc=ZGg1OTk1ODZmNzM7aGczO0Bpank2NDw6ZmdlZzMzZjgzM0AvLmNfYS4uNS8xNjFeNjUzYSNfbnMwcjQwMmJgLS1kL2Nzcw%3D%3D\u0026l=2022110908402001024501106913087F41\u0026btag=80000",
                                "https://v16-webapp.tiktok.com/29cab804f5e93ac94964d941c424a7f8/636bbbe1/video/tos/useast2a/tos-useast2a-pve-0037-aiso/8abe21a3ddfa49fba5f86bd9a4333f2d/?a=1988\u0026ch=0\u0026cr=0\u0026dr=0\u0026lr=tiktok\u0026cd=0%7C0%7C1%7C0\u0026cv=1\u0026br=4130\u0026bt=2065\u0026cs=0\u0026ds=3\u0026ft=_GC~MBMyq8Z48IYhe2NM4Qml7GbRyu8\u0026mime_type=video_mp4\u0026qs=0\u0026rc=ZGg1OTk1ODZmNzM7aGczO0Bpank2NDw6ZmdlZzMzZjgzM0AvLmNfYS4uNS8xNjFeNjUzYSNfbnMwcjQwMmJgLS1kL2Nzcw%3D%3D\u0026l=2022110908402001024501106913087F41\u0026btag=80000"
                            ]
                        },
                        "QualityType": 10
                    }
                ],
                "codecType": "h264",
                "cover": "https://p16-sign-va.tiktokcdn.com/obj/tos-useast2a-p-0037-aiso/ae70d8dfc60f46569bc5998fa39af12c_1667019453?x-expires=1668002400\u0026x-signature=vrflkJIhB8%2B%2BMDz6ZSuGRoPlMv8%3D",
                "definition": "720p",
                "downloadAddr": "https://v16-webapp.tiktok.com/29cab804f5e93ac94964d941c424a7f8/636bbbe1/video/tos/useast2a/tos-useast2a-pve-0037-aiso/8abe21a3ddfa49fba5f86bd9a4333f2d/?a=1988\u0026ch=0\u0026cr=0\u0026dr=0\u0026lr=tiktok\u0026cd=0%7C0%7C1%7C0\u0026cv=1\u0026br=4130\u0026bt=2065\u0026cs=0\u0026ds=3\u0026ft=_GC~MBMyq8Z48IYhe2NM4Qml7GbRyu8\u0026mime_type=video_mp4\u0026qs=0\u0026rc=ZGg1OTk1ODZmNzM7aGczO0Bpank2NDw6ZmdlZzMzZjgzM0AvLmNfYS4uNS8xNjFeNjUzYSNfbnMwcjQwMmJgLS1kL2Nzcw%3D%3D\u0026l=2022110908402001024501106913087F41\u0026btag=80000",
                "duration": 13,
                "dynamicCover": "https://p16-sign-va.tiktokcdn.com/obj/tos-useast2a-p-0037-aiso/08b2dcf65f384c109d1d4832496b8387_1667019454?x-expires=1668002400\u0026x-signature=0aDaYsei2vg5vkC72Pc%2BpxUxqTI%3D",
                "encodeUserTag": "",
                "encodedType": "normal",
                "format": "mp4",
                "height": 1024,
                "id": "7159794001544056091",
                "originCover": "https://p16-sign-va.tiktokcdn.com/obj/tos-useast2a-p-0037-aiso/a59da7f54581411b86682a9396bcba1a_1667019454?x-expires=1668002400\u0026x-signature=iDGu1u4bNIJdSmM4WrwOWPem9gI%3D",
                "playAddr": "https://v16-webapp.tiktok.com/29cab804f5e93ac94964d941c424a7f8/636bbbe1/video/tos/useast2a/tos-useast2a-pve-0037-aiso/8abe21a3ddfa49fba5f86bd9a4333f2d/?a=1988\u0026ch=0\u0026cr=0\u0026dr=0\u0026lr=tiktok\u0026cd=0%7C0%7C1%7C0\u0026cv=1\u0026br=4130\u0026bt=2065\u0026cs=0\u0026ds=3\u0026ft=_GC~MBMyq8Z48IYhe2NM4Qml7GbRyu8\u0026mime_type=video_mp4\u0026qs=0\u0026rc=ZGg1OTk1ODZmNzM7aGczO0Bpank2NDw6ZmdlZzMzZjgzM0AvLmNfYS4uNS8xNjFeNjUzYSNfbnMwcjQwMmJgLS1kL2Nzcw%3D%3D\u0026l=2022110908402001024501106913087F41\u0026btag=80000",
                "ratio": "720p",
                "reflowCover": "https://p16-sign-va.tiktokcdn.com/obj/tos-useast2a-p-0037-aiso/ae70d8dfc60f46569bc5998fa39af12c_1667019453?x-expires=1668002400\u0026x-signature=vrflkJIhB8%2B%2BMDz6ZSuGRoPlMv8%3D",
                "shareCover": [
                    "",
                    "https://p16-sign-va.tiktokcdn.com/tos-useast2a-p-0037-aiso/a59da7f54581411b86682a9396bcba1a_1667019454~tplv-tiktok-play.jpeg?x-expires=1668585600\u0026x-signature=CeKvSh5GGRpNGgqDTmE%2BJbWJfeE%3D",
                    "https://p16-sign-va.tiktokcdn.com/tos-useast2a-p-0037-aiso/a59da7f54581411b86682a9396bcba1a_1667019454~tplv-tiktokx-share-play.jpeg?x-expires=1668585600\u0026x-signature=dS0NGuYjX8fEOAT4HSpQeozDk8Q%3D"
                ],
                "videoQuality": "normal",
                "volumeInfo": {
                    "Loudness": -6,
                    "Peak": 1
                },
                "width": 576,
                "zoomCover": {
                    "240": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-p-0037-aiso/ae70d8dfc60f46569bc5998fa39af12c_1667019453~tplv-f5insbecw7-1:240:240.jpeg?x-expires=1668002400\u0026x-signature=EVjMUtTuppzMpUuHlIGxqnEF4Mc%3D",
                    "480": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-p-0037-aiso/ae70d8dfc60f46569bc5998fa39af12c_1667019453~tplv-f5insbecw7-1:480:480.jpeg?x-expires=1668002400\u0026x-signature=JmWRsmTOa6sQ5LD4KzqwpBRrzWA%3D",
                    "720": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-p-0037-aiso/ae70d8dfc60f46569bc5998fa39af12c_1667019453~tplv-f5insbecw7-1:720:720.jpeg?x-expires=1668002400\u0026x-signature=lInygn6YeQvkUIXMAMz6ovqZZjk%3D",
                    "960": "https://p16-sign-va.tiktokcdn.com/tos-useast2a-p-0037-aiso/ae70d8dfc60f46569bc5998fa39af12c_1667019453~tplv-f5insbecw7-1:960:960.jpeg?x-expires=1668002400\u0026x-signature=jTrqem%2FxgJYaalwkeeIK%2FIQQftU%3D"
                }
            },
            "vl1": false
        },
    ],
    "log_pb": {
        "impr_id": "2022110908402001024501106913087F41"
    },
    "statusCode": 0,
    "status_code": 0
}
```