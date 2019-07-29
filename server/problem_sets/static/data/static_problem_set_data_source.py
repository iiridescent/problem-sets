from abc import ABC, abstractmethod

from problem_sets.static.static_problem_set import StaticProblemSet


class StaticProblemSetDataSource(ABC):
    @abstractmethod
    def create(self, data: StaticProblemSet):
        pass

    @abstractmethod
    def get(self, id: str) -> StaticProblemSet:
        pass

    @abstractmethod
    def delete(self, id: str):
        pass

    @abstractmethod
    def update(self, id: str, data: StaticProblemSet):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def check_id_available(self, id: str) -> bool:
        pass
