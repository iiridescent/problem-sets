#  Copyright (c) 2019 Thomas Howe

from abc import ABC, abstractmethod


class SQLiteSerializable(ABC):
    @abstractmethod
    def to_sqlite_row(cls):
        pass

    @classmethod
    @abstractmethod
    def from_sqlite_row(cls):
        pass
