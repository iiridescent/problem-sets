#  Copyright (c) 2019 Thomas Howe

from abc import ABC, abstractmethod

from problem_sets.static.static_problem_entity import StaticProblemEntity


class StaticProblemDataSource(ABC):
    @abstractmethod
    def create(self, data: StaticProblemEntity):
        pass

    @abstractmethod
    def get(self, id: int) -> StaticProblemEntity:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def update(self, id: int, data: StaticProblemEntity):
        pass

    @abstractmethod
    def pick_problem_from_set(self, set_id: str):
        pass

    @abstractmethod
    def list_problems_from_set(self, set_id: str):
        pass
