#  Copyright (c) 2019 Thomas Howe

from abc import ABC, abstractmethod
from sqlite3 import Connection

from problem_sets.static.data.sqlite import sqlite_util


class SQLiteRepository(ABC):

    def __init__(self, connection: Connection, table: str):
        self.connection = connection
        self.table = table,
        self.setup()

    @abstractmethod
    def setup(self):
        pass

    def select_by_id(self, id: any):
        select_by_id_command = f"""SELECT * FROM {self.table} WHERE id=?
        """
        result = sqlite_util.query_fetch(self.connection, select_by_id_command, (id,))

        if len(result) == 0:
            return None

        return result[0]
