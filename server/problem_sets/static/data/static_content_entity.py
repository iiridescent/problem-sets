from dataclasses import dataclass
from enum import Enum
from typing import Optional

from problem_sets.serialization import Serializable


class StaticContentType(Enum):
    text = "text"
    image = "image"


@dataclass
class StaticContentEntity(Serializable):
    id: Optional[int]
    type: StaticContentType
    value: str

    def serialize(self) -> dict:
        serialized = self.__dict__
        serialized.type = serialized['type'].value
        return serialized

    @classmethod
    def deserialize(cls, serialized: dict):
        serialized = serialized.copy()
        serialized['type'] = StaticContentType(serialized['type'])
        cls(**serialized)
