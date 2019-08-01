from abc import ABC
from typing import Union

from problem_sets.serialization import Serializable


class Problem(Serializable, ABC):
    def __init__(
            self,
            set_id: str,
            id: Union[str, int],
            format: str
    ):
        """
        The output of a generated problem
        """

        self.set_id = set_id
        self.id = id
        self.format = format

    def serialize(self) -> dict:
        """JSON form for API"""
        return {
            "id": self.id,
            "setId": self.set_id,
            "format": self.format,
        }

    @classmethod
    def deserialize(cls, serialized: dict):
        pass
