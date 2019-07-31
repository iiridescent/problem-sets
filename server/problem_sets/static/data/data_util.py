#  Copyright (c) 2019 Thomas Howe
import os

from PIL import Image
from typing import List


def create_image(data: Image, path: str):
    data.save(path)


def delete_image(path: str):
    return os.remove(path)


def get_image(path: str) -> Image:
    return Image.open(path)