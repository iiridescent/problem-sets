#  Copyright (c) 2019 Thomas Howe

import sqlite3

from problem_sets.static.data.sqlite import sqlite_util
from problem_sets.static.data.sqlite.sqlite_repository import SQLiteRepository
from problem_sets.static.data.static_problem_data_source import StaticProblemDataSource
from problem_sets.static.static_problem_entity import StaticProblemEntity

PROBLEMS_TABLE_ID = "problems"


class StaticProblemSQLiteRepository(SQLiteRepository, StaticProblemDataSource):

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection, PROBLEMS_TABLE_ID)

    def create(self, data: StaticProblemEntity):
        create_problem_command = """INSERT INTO problems (set_id, used) VALUES (?, ?)"""
        sqlite_util.write_commit(self.connection, create_problem_command, (data.set_id, data.used))

    def get(self, id: int) -> StaticProblemEntity:
        get_problem_command = """SELECT * FROM problems WHERE id=?
        """
        result = sqlite_util.query_fetch(self.connection, get_problem_command, (id,))

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
        create_table_command = """CREATE TABLE IF NOT EXISTS problems (
                                        id integer PRIMARY KEY,
                                        set_id text NOT NULL,
                                        used Boolean NOT NULL,
                                        FOREIGN KEY (set_id) REFERENCES problem_sets(id)
                                        ON UPDATE CASCADE ON DELETE CASCADE
                                    );"""
        sqlite_util.write_commit(self.connection, create_table_command)
