#  Copyright (c) 2019 Thomas Howe

from problem_sets.serialization import Serializable


class StaticAnswerPageEntity(Serializable):

    def __init__(self, set_id: str, id: str):
        self.set_id = set_id
        self.id = id

    def serialize(self) -> dict:
        return {
            "set_id": self.set_id,
            "id": self.id
        }
