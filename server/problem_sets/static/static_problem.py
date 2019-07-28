from typing import Union

from problem_sets.problem import Problem

STATIC_FORMAT = "static"


class StaticProblem(Problem):
    def __init__(self, set_id: str, id: str, used: bool = False):
        super().__init__(set_id, id, STATIC_FORMAT)

        self.used = used

    def serialize(self):
        data = super(StaticProblem, self).serialize().copy()

        data["used"] = self.used

        return data
