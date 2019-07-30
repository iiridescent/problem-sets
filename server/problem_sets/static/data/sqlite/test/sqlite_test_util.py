#  Copyright (c) 2019 Thomas Howe

import os
from sqlite3 import Connection

from typing import List, Union

from problem_sets.dir_util import ROOT_DIR
from problem_sets.static.data import data_util
from problem_sets.static.data.sqlite import sqlite_manager, sqlite_util
from problem_sets.static.data.sqlite.sqlite_util import connection

TEST_DB_PATH = data_util.DATA_DIR = os.path.join(ROOT_DIR, "test_static_data", "test_static.db")

conn: Connection = None


def clean_start(tables: Union[str, List[str]]):
    # Make sure the DB is clean before we start
    global conn

    conn = connection(TEST_DB_PATH)

    sqlite_manager.initialize(TEST_DB_PATH)

    if isinstance(tables, str):
        drop_table_if_exists(conn, tables)
    elif isinstance(tables, list) and all(isinstance(n, str) for n in tables):
        for table in tables:
            drop_table_if_exists(conn, table)

    sqlite_manager.initialize(TEST_DB_PATH)


def drop_table_if_exists(conn: Connection, table_name: str):
    command_drop_table = f"""DROP TABLE IF EXISTS {table_name}
    """
    sqlite_util.write_commit(conn, command_drop_table)
