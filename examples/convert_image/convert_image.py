"""
Put this script in your PATH
"""

import sys
from pathlib import Path

from PIL import Image

SUPPORTED_EXT = [
    "ico",
    "png",
    "jpeg",
    "bmp",
]


def main():
    if len(sys.argv) != 3:
        print(f"Usage: python convert_image.py <path_to_img> [{'|'.join(SUPPORTED_EXT)}]")
        return

    img_path = Path(sys.argv[1])
    convert_to = sys.argv[2].strip(".").lower()
    if convert_to not in SUPPORTED_EXT:
        raise ValueError(f"Available extensions: {'|'.join(SUPPORTED_EXT)}")

    im = get_image_from_path(img_path)

    im.save(img_path.with_suffix(f".{convert_to}"), format=convert_to)


def get_image_from_path(path: Path) -> Image.Image:
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist. {path=}")
    if not path.is_file():
        raise ValueError(f"Path is not a directory. {path=}")

    return Image.open(path)


if __name__ == '__main__':
    main()
