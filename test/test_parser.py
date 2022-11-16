import json

from tiktok_trending import parse_item


def test_parse_post():
    with open("test/response.json") as fh:
        data: dict = json.load(fh)

    item = data.get("itemList", [{}])[0]
    post = parse_item(item)

    assert post.author.id == "6628475227129610242"
    assert post.video.id == "7158770362770099483"


def test_missing_fields():
    # Missing "bitrateInfo" for Video.
    with open("test/item_6567681775181971457_7164031309466078465.json") as fh:
        item = json.load(fh)
    parse_item(item)

    # Missing "album", "authorName", "duration" for Music.
    with open("test/item_6609102694261522434_7165346556386839834.json") as fh:
        item = json.load(fh)
    parse_item(item)


def test_extra_fields():
    # Unexpected keyword "scheduleSearchTime" for Music.
    with open("test/item_6742459250268832769_7166174024223952130.json") as fh:
        item = json.load(fh)
    parse_item(item)
