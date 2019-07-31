#  Copyright (c) 2019 Thomas Howe
from dataclasses import dataclass

from typing import List, Optional

from problem_sets.serialization import Serializable, serialize_recursive
from problem_sets.static.data.static_content_entity import StaticContentEntity


@dataclass
class StaticProblemSetEntity(Serializable):
    id: str
    source: str
    instruction_contents: Optional[List[StaticContentEntity]]
    answer_contents: Optional[List[StaticContentEntity]]

    def serialize(self) -> dict:
        return serialize_recursive(self)

    @classmethod
    def deserialize(cls, serialized: dict):
        pass