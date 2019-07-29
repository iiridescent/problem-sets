from abc import ABC, abstractmethod

from problem_sets.static.static_problem import StaticProblem


class StaticProblemDataSource(ABC):
    @abstractmethod
    def create(self, data: StaticProblem):
        raise NotImplementedError("'create' is not implemented")

    @abstractmethod
    def get(self, id: str) -> StaticProblem:
        raise NotImplementedError("'get' is not implemented")

    @abstractmethod
    def delete(self, id: str):
        raise NotImplementedError("'delete' is not implemented")

    @abstractmethod
    def update(self, id: str, data: StaticProblem):
        raise NotImplementedError("'update' is not implemented")
