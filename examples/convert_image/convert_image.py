"""
This script should be in your PATH because our
context menu uses the script for converting images
"""

import sys
from enum import StrEnum
from pathlib import Path

from PIL import Image


class ImageType(StrEnum):
    ICO = "ico"
    PNG = "png"
    JPEG = "jpeg"
    BMP = "bmp"
    WEBP = "webp"


SUPPORTED_IMAGE_TYPES = [
    ImageType.ICO,
    ImageType.PNG,
    ImageType.JPEG,
    ImageType.BMP,
    ImageType.WEBP,
]

IMAGE_TYPES_WITHOUT_ALPHA = [
    ImageType.JPEG,
    ImageType.WEBP
]


def main():
    if len(sys.argv) != 3:
        print(f"Usage: python convert_image.py <path_to_img> <{ ' | '.join(SUPPORTED_IMAGE_TYPES)}>")
        return

    img_path = Path(sys.argv[1])
    convert_to = sys.argv[2].strip(".").lower()
    if convert_to not in SUPPORTED_IMAGE_TYPES:
        raise ValueError(f"Available extensions: {' | '.join(SUPPORTED_IMAGE_TYPES)}")

    im = get_image_from_path(img_path)

    if convert_to in IMAGE_TYPES_WITHOUT_ALPHA:
        im = im.convert("RGB")

    im.save(img_path.with_suffix(f".{convert_to}"), format=convert_to)


def get_image_from_path(path: Path) -> Image.Image:
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist. {path=}")

    if not path.is_file():
        raise ValueError(f"Path is not a directory. {path=}")

    return Image.open(path)


if __name__ == '__main__':
    main()
