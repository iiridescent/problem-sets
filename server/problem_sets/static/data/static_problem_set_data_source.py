#  Copyright (c) 2019 Thomas Howe

from abc import ABC, abstractmethod
from typing import Optional, List

from problem_sets.static.data.static_problem_set_entity import StaticProblemSetEntity


class StaticProblemSetDataSource(ABC):
    @abstractmethod
    def create(self, data: StaticProblemSetEntity):
        pass

    @abstractmethod
    def get(self, id: str) -> Optional[StaticProblemSetEntity]:
        pass

    @abstractmethod
    def delete(self, id: str):
        pass

    @abstractmethod
    def update(self, id: str, data: StaticProblemSetEntity):
        pass

    @abstractmethod
    def list(self) -> Optional[List[StaticProblemSetEntity]]:
        pass

    @abstractmethod
    def check_id_available(self, id: str) -> bool:
        pass