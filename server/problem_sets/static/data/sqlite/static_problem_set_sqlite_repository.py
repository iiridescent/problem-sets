#  Copyright (c) 2019 Thomas Howe

import sqlite3

from problem_sets.static.data.sqlite import sqlite_util
from problem_sets.static.data.sqlite.sqlite_repository import SQLiteRepository
from problem_sets.static.data.static_problem_set_data_source import StaticProblemSetDataSource
from problem_sets.static.static_problem_set_entity import StaticProblemSetEntity

PROBLEM_SETS_TABLE_ID = "problem_sets"


class StaticProblemSetSQLiteRepository(SQLiteRepository, StaticProblemSetDataSource):

    def __init__(self, connection: sqlite3.Connection):
        super().__init__(connection, PROBLEM_SETS_TABLE_ID)

    def create(self, data: StaticProblemSetEntity):
        create_problem_set_command = """INSERT INTO problem_sets (id, source) VALUES (?, ?)
        """
        sqlite_util.write_commit(self.connection, create_problem_set_command,
                                 (data.id, data.source))

    def get(self, id: str) -> StaticProblemSetEntity:
        get_problem_set_command = """SELECT * FROM problem_sets WHERE id=?
        """
        result = sqlite_util.query_fetch(self.connection, get_problem_set_command, (id,))

        if len(result) == 0:
            return None

        row = result[0]

        return StaticProblemSetEntity(**row)

    def delete(self, id: str):
        pass

    def update(self, id: str, data: StaticProblemSetEntity):
        pass

    def list(self):
        get_problem_sets_command = """SELECT id FROM ? ORDER BY ROWID DESC
        """
        result = sqlite_util.query_fetch(self.connection, get_problem_sets_command, (PROBLEM_SETS_TABLE_ID,))

    def check_id_available(self, id: str) -> bool:
        check_id_command = """SELECT id FROM problem_sets WHERE id=?
        """
        result = sqlite_util.query_fetch(self.connection, check_id_command, (id,))
        return len(result) == 0

    def setup(self):
        create_table_command = """CREATE TABLE IF NOT EXISTS problem_sets (
                                        id TEXT PRIMARY KEY,
                                        source TEXT
                                    );"""
        sqlite_util.write_commit(self.connection, create_table_command)

    @staticmethod
    def row_to_problem_set(row):
        id = row[0]
        source = row[1]
        return StaticProblemSetEntity(id, source)
