#  Copyright (c) 2019 Thomas Howe

from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Session

PROBLEMS_TABLE_ID = "problem"

from problem_sets.static.data.sqlite import sqlite_util
from problem_sets.static.data.sqlite.sqlite_manager import Base
from problem_sets.static.data.sqlite.sqlite_repository import SQLiteRepository
from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import PROBLEM_SETS_TABLE_ID
from problem_sets.static.data.static_problem_data_source import StaticProblemDataSource
from problem_sets.static.static_problem_entity import StaticProblemEntity


@dataclass
class StaticProblemRow(Base):
    __tablename__ = PROBLEMS_TABLE_ID
    id = Column(Integer, primary_key=True)
    set_id = Column(String, ForeignKey(f"{PROBLEM_SETS_TABLE_ID}.id"))
    used = Column(Boolean)

    def __init__(self, id: str, set_id: str, used: bool):
        self.id = id
        self.set_id = set_id
        self.used = used


class StaticProblemSQLiteRepository(SQLiteRepository, StaticProblemDataSource):

    def __init__(self, session: Session):
        super().__init__(session, StaticProblemRow)

    def create(self, data: StaticProblemEntity):
        create_problem_command = """INSERT INTO problems (set_id, used) VALUES (?, ?)"""
        sqlite_util.write_commit(self.session, create_problem_command, (data.set_id, data.used))

    def get(self, id: int) -> StaticProblemEntity:
        get_problem_command = """SELECT * FROM problems WHERE id=?
        """
        result = sqlite_util.query_fetch(self.session, get_problem_command, (id,))

        if len(result) == 0:
            return None

        row = result[0]

        return StaticProblemEntity(**row)

    def delete(self, id: int):
        pass

    def update(self, id: int, data: StaticProblemEntity):
        pass

    def pick_problem_from_set(self, set_id: str):
        pass

    def list_problems_from_set(self, set_id: str):
        pass

    def setup(self):
        # create_table_command = """CREATE TABLE IF NOT EXISTS problems (
        #                                 id integer PRIMARY KEY,
        #                                 set_id text NOT NULL,
        #                                 used Boolean NOT NULL,
        #                                 FOREIGN KEY (set_id) REFERENCES problem_sets(id)
        #                                 ON UPDATE CASCADE ON DELETE CASCADE
        #                             );"""
        # sqlite_util.write_commit(self.session, create_table_command)
        pass

    @staticmethod
    def map_row_to_entity(row: Base):
        pass

    @staticmethod
    def map_entity_to_row(entity):
        pass
