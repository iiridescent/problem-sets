#  Copyright (c) 2019 Thomas Howe
from problem_sets.serialization import Serializable


class StaticProblemSetEntity(Serializable):
    def __init__(self, id: str, source: str):
        self.id = id
        self.source = source

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "source": self.source
        }
