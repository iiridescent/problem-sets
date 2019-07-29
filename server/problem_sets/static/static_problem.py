from typing import List

from problem_sets.problem import Problem
from problem_sets.widget import Widget

STATIC_FORMAT = "static"


class StaticProblem(Problem):
    def __init__(self, set_id: str, id: str, content: List[Widget], used: bool = False):
        super().__init__(set_id, id, STATIC_FORMAT)

        self.used = used
        self.content = content

    def serialize(self) -> dict:
        data = super(StaticProblem, self).serialize().copy()

        data = {**data, "used": self.used}

        return data
