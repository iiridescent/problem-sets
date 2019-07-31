#  Copyright (c) 2019 Thomas Howe
from dataclasses import dataclass
from typing import List, Optional

from problem_sets.serialization import Serializable, serialize_recursive
from problem_sets.static.data.static_content_entity import StaticContentEntity

STATIC_FORMAT = "static"


@dataclass
class StaticProblemEntity(Serializable):
    id: int
    set_id: str
    used: bool
    content: Optional[List[StaticContentEntity]]

    def serialize(self) -> dict:
        data = self.__dict__

        if self.content:
            data['content'] = serialize_recursive(self.content)

        return data

    @classmethod
    def deserialize(cls, serialized: dict):
        # TODO deserialize in StaticProblemEntity doesn't do anything
        raise NotImplementedError(f"'deserialize' isn't implemented in '{cls.__name__}'")
