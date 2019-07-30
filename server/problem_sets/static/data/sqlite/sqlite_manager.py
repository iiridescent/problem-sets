#  Copyright (c) 2019 Thomas Howe

import os

import sqlalchemy as sql
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from problem_sets.static.data.data_util import DATA_DIR
from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import StaticProblemSetSQLiteRepository
from problem_sets.static.data.sqlite.static_problem_sqlite_repository import StaticProblemSQLiteRepository

DB_PATH = os.path.join(DATA_DIR, "static.db")

static_problem_set_repo: StaticProblemSetSQLiteRepository = None
static_problem_repo: StaticProblemSQLiteRepository = None
# static_answer_page_repo: StaticAnswerPageSQLiteRepository = None

db: sql.engine = None
db_meta: sql.MetaData = None

Base = declarative_base()

Session: sql.orm.sessionmaker = None


def initialize(db_path: str = None):
    global db, db_meta, Session
    db_path = db_path if db_path is not None else DB_PATH
    # TODO see if I can get rid of this call because SQLAlchemy handles it
    # sqlite_util.sqlite_touch(db_path)
    db = sql.create_engine(f"sqlite:///{db_path}")
    db.echo = True
    db_meta = MetaData()
    Session = sessionmaker(db)
    init_repos(db)


def init_repos(engine: sql.engine.Engine):
    global static_problem_set_repo, static_problem_repo, static_answer_page_repo
    Base.metadata.create_all(engine)
    session = Session()
    static_problem_set_repo = StaticProblemSetSQLiteRepository(session)
    static_problem_repo = StaticProblemSQLiteRepository(session)
    # static_answer_page_repo = StaticAnswerPageSQLiteRepository(conn)
