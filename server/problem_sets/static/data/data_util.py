#  Copyright (c) 2019 Thomas Howe
import os


def delete_file(path: str):
    return os.remove(path)


def get_bytes_file(path: str) -> bytes:
    with open(path, "rb") as file:
        return bytes(file.read())


def write_bytes_file(path: str, data: bytes):
    file = open(path, "wb")
    file.write(data)
    file.close()
