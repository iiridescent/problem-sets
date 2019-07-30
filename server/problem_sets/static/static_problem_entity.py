#  Copyright (c) 2019 Thomas Howe

from problem_sets.serialization import Serializable

STATIC_FORMAT = "static"


class StaticProblemEntity(Serializable):
    def __init__(self, id: int = None, set_id: str = None, used: bool = False):
        self.id = id
        self.set_id = set_id
        self.used = used

    def serialize(self) -> dict:
        data = super(StaticProblemEntity, self).serialize().copy()

        data = {"set_id": self.set_id, "id": self.id, "used": self.used}

        return data
