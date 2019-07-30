#  Copyright (c) 2019 Thomas Howe

from abc import ABC, abstractmethod

from problem_sets.static.static_problem_set_entity import StaticProblemSetEntity


class StaticProblemSetDataSource(ABC):
    @abstractmethod
    def create(self, data: StaticProblemSetEntity):
        pass

    @abstractmethod
    def get(self, id: str) -> StaticProblemSetEntity:
        pass

    @abstractmethod
    def delete(self, id: str):
        pass

    @abstractmethod
    def update(self, id: str, data: StaticProblemSetEntity):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def check_id_available(self, id: str) -> bool:
        pass
