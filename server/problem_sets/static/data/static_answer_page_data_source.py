#  Copyright (c) 2019 Thomas Howe

from abc import ABC, abstractmethod

from problem_sets.static.static_answer_page_entity import StaticAnswerPageEntity


class StaticAnswerPageDataSource(ABC):
    @abstractmethod
    def create(self, data: StaticAnswerPageEntity):
        pass

    @abstractmethod
    def get(self, id: str) -> StaticAnswerPageEntity:
        pass

    @abstractmethod
    def delete(self, id: str):
        pass
