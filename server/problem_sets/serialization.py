from abc import ABC, abstractmethod
from inspect import isclass
from types import FunctionType


class Serializable(ABC):
    @abstractmethod
    def serialize(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def deserialize(cls, serialized: dict):
        pass


def _serialize_func(serializable: Serializable):
    return serializable.serialize()


def _list_serializable_dict(val: dict, func: FunctionType = _serialize_func) -> dict:
    serialized = {}
    # noinspection PyTypeChecker
    for key, value in val.items():
        serialized_value = _recursive_serializable_lambda(value, func)
        serialized[key] = serialized_value

    return serialized


def _list_serializable_lambda(val: list, func: FunctionType = _serialize_func) -> list:
    return list(_recursive_serializable_lambda(item, func) for item in val)


def _recursive_serializable_lambda(val: any, func: FunctionType = _serialize_func):
    if isinstance(val, Serializable):
        return func(val)

    if isinstance(val, list):
        return _list_serializable_lambda(val, func)

    if isinstance(val, dict):
        return _list_serializable_dict(val, func)

    if isclass(val):
        return _list_serializable_dict(val.__dict__, func)

    return val


def serialize_recursive(val: any):
    return _recursive_serializable_lambda(val, _serialize_func)
