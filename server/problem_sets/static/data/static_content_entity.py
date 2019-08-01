from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

from problem_sets.serialization import Serializable


class StaticContentEntityType(Enum):
    text = "text"
    image = "image"


@dataclass
class StaticContentEntity(Serializable):
    type: StaticContentEntityType
    value: Optional[Union[str, bytes]] = None
    id: Optional[int] = None

    def serialize(self) -> dict:
        serialized = self.__dict__
        serialized['type'] = self.type.value
        if self.value is None:
            # We don't want a null value for 'value' if it's an image
            del serialized['value']
        return serialized

    @classmethod
    def deserialize(cls, serialized: dict):
        serialized = serialized.copy()
        serialized['type'] = StaticContentEntityType(serialized['type'])
        cls(**serialized)
