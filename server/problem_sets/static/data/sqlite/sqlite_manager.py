#  Copyright (c) 2019 Thomas Howe

import os
from sqlite3 import Connection, Row

from problem_sets.static.data.data_util import DATA_DIR
from problem_sets.static.data.sqlite import sqlite_util
from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import StaticProblemSetSQLiteRepository
from problem_sets.static.data.sqlite.static_problem_sqlite_repository import StaticProblemSQLiteRepository

DB_PATH = os.path.join(DATA_DIR, "static.db")

static_problem_set_repo: StaticProblemSetSQLiteRepository = None
static_problem_repo: StaticProblemSQLiteRepository = None
# static_answer_page_repo: StaticAnswerPageSQLiteRepository = None

conn: Connection = None


def initialize(db_path: str = None):
    global conn
    db_path = db_path if db_path is not None else DB_PATH
    sqlite_util.sqlite_touch(db_path)
    conn = sqlite_util.connection(db_path)
    conn.row_factory = Row
    init_repos(conn)


def init_repos(conn: Connection):
    global static_problem_set_repo, static_problem_repo, static_answer_page_repo
    static_problem_set_repo = StaticProblemSetSQLiteRepository(conn)
    static_problem_repo = StaticProblemSQLiteRepository(conn)
    # static_answer_page_repo = StaticAnswerPageSQLiteRepository(conn)
