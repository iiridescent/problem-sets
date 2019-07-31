#  Copyright (c) 2019 Thomas Howe

import os
from sqlite3 import Connection
from typing import List, Union

from problem_sets.dir_util import ROOT_DIR
from problem_sets.static.data import data_util
from problem_sets.static.data.sqlite import sqlite_manager, sqlite_util
from problem_sets.static.data.sqlite.sqlite_util import connection
from problem_sets.static.data.sqlite.static_content_sqlite_repository import StaticContentRow, \
    static_content_problem_association, static_content_answer_problem_set_association, \
    static_content_instruction_problem_set_association
from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import StaticProblemSetRow
from problem_sets.static.data.sqlite.static_problem_sqlite_repository import StaticProblemRow

TEST_DB_PATH = data_util.DATA_DIR = os.path.join(ROOT_DIR, "test_static_data", "test_static.db")

conn: Connection = None

drop_tables_list = [StaticProblemRow.__tablename__, StaticProblemSetRow.__tablename__, StaticContentRow.__tablename__,
                    static_content_problem_association.name, static_content_answer_problem_set_association.name,
                    static_content_instruction_problem_set_association.name]


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
