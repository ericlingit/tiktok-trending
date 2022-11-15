import argparse
import json
import sys
from pathlib import Path

from . import get_new_posts, parse_response, download_video


def main() -> None:
    """
    Options:
    - Save Tiktok vidoes to dir; pwd if not specified.
    - Save video metadata.
    - Skip parsing and downloading, and dump raw JSON response from Tiktok.
    """
    parser = argparse.ArgumentParser(
        prog="tiktok_trending",
        description="Download Tiktok trending videos.",
    )
    # Output dir.
    parser.add_argument(
        "-d",
        "--dir",
        action="store",
        default=".",
        required=False,
        help="the output directory. Defaults to the current working directory",
    )
    # Save video metadata.
    parser.add_argument(
        "-m",
        "--metadata",
        action="store_true",
        required=False,
        help="whether to save video metadata as JSON files",
    )
    # Skip parsing and dump raw response JSON.
    parser.add_argument(
        "-s",
        "--skip-download",
        action="store_true",
        required=False,
        help="don't download video; dump the raw JSON response from Tiktok",
    )
    args = parser.parse_args()

    out_dir = Path(getattr(args, "dir", ".")).resolve()
    save_metadata = getattr(args, "metadata", False)
    skip_download: bool = getattr(args, "skip_download", False)

    if not out_dir.is_dir():
        sys.exit(f"error: not a directory: {out_dir.as_posix()}")

    resp = get_new_posts()
    if skip_download:
        with (out_dir / "tiktok_response.json").open("w") as f_resp:
            json.dump(resp, f_resp, ensure_ascii=False, indent=4)
        return

    tiks = parse_response(resp)
    for tik in tiks:
        download_video(
            tik,
            out_dir,
            f"tiktok_{tik.author.id}_{tik.video.id}",
            save_metadata,
        )
        break


if __name__ == "__main__":
    main()
