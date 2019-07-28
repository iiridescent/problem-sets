from abc import ABC

from problem_sets.static.static_problem import StaticProblem


class StaticProblemDataSource(ABC):
    def create(self, data: StaticProblem):
        raise NotImplementedError("'create' is not implemented")

    def get(self, id: str) -> StaticProblem:
        raise NotImplementedError("'get' is not implemented")

    def delete(self, id: str):
        raise NotImplementedError("'delete' is not implemented")

    def update(self, id: str, data: StaticProblem):
        raise NotImplementedError("'update' is not implemented")