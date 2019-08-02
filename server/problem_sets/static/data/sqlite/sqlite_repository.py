#  Copyright (c) 2019 Thomas Howe

from abc import ABC, abstractmethod
from typing import Union, List

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session

from problem_sets.static.data.sqlite.sqlite_manager import Base


class SQLiteRepository(ABC):
    session = None
    row_class = None

    def __init__(self, session: scoped_session):
        self.session = session

    @staticmethod
    @abstractmethod
    def map_row_to_entity(row: Base):
        pass

    @staticmethod
    @abstractmethod
    def map_entity_to_row(entity):
        pass

    def db_find_by_id(self, id: any):
        return self.session.query(self.row_class).get(id)

    def db_list(self):
        return self.session.query(self.row_class).all()

    def db_insert(self, rows: Union[List[Base], Base]):
        if isinstance(rows, Base):
            self.session.add(rows)
        elif isinstance(rows, list) and all(isinstance(n, Base) for n in rows):
            self.session.add_all(rows)
        self.db_commit_or_rollback()

    def db_delete(self, id: str):
        item = self.session.query(self.row_class).get(id)
        self.session.delete(item)
        self.db_commit_or_rollback()
        return

    def db_commit_or_rollback(self):
        try:
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            raise

    @classmethod
    def db_map_row_to_entities(cls, rows: Union[Base, List[Base]]):
        if isinstance(rows, list):
            entities = []
            for row in rows:
                if not isinstance(row, cls.row_class):
                    continue
                entities.append(cls.map_row_to_entity(row))
            return entities
        elif isinstance(rows, cls.row_class):
            return cls.map_row_to_entity(rows)
