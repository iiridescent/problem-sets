from abc import ABC, abstractmethod
from inspect import isclass


class Serializable(ABC):
    @abstractmethod
    def serialize(self) -> dict:
        pass


def serialize_dict(val: dict) -> dict:
    serialized = {}
    # noinspection PyTypeChecker
    for key, value in val.items():
        serialized_value = serialize_recursive(value)
        serialized[key] = serialized_value

    return serialized


def serialize_list(val: list) -> list:
    return list(serialize_recursive(item) for item in val)


def serialize_recursive(val: any):
    if isinstance(val, Serializable):
        return val.serialize()

    if isinstance(val, list):
        return serialize_list(val)

    if isinstance(val, dict):
        return serialize_dict(val)

    if isclass(val):
        return serialize_dict(val.__dict__)

    return val
