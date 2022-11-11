import json

from tiktok_trending import parse_item


def test_parse_post():
    with open("test/response.json") as fh:
        data: dict = json.load(fh)

    item = data.get("itemList", [{}])[0]
    post = parse_item(item)

    assert post.author.id == "6628475227129610242"
    assert post.video.id == "7158770362770099483"
