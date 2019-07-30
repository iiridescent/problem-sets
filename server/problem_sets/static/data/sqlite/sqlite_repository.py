#  Copyright (c) 2019 Thomas Howe

from abc import ABC, abstractmethod

from sqlalchemy.orm import Session
from typing import Union, List

from problem_sets.static.data.sqlite.sqlite_manager import Base


class SQLiteRepository(ABC):

    def __init__(self, session: Session, row_class: Base):
        self.session = session
        self.row_class = row_class
        self.setup()

    @abstractmethod
    def setup(self):
        pass

    @staticmethod
    @abstractmethod
    def map_row_to_entity(row: Base):
        pass

    @staticmethod
    @abstractmethod
    def map_entity_to_row(entity):
        pass

    def find_by_id(self, id: any):
        return self.session.query(self.row_class).get(id)

    def insert(self, rows: Union[List[Base], Base]):
        if isinstance(rows, Base):
            self.session.add(rows)
        elif isinstance(rows, list) and all(isinstance(n, Base) for n in rows):
            self.session.add_all(rows)
        self.session.commit()
