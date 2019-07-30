#  Copyright (c) 2019 Thomas Howe

import os

import sqlalchemy as sql
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

# Base must be created before these are imported
from problem_sets.static.data.data_manager import DATA_DIR
from problem_sets.static.data.sqlite.static_problem_sqlite_repository import StaticProblemSQLiteRepository
from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import StaticProblemSetSQLiteRepository

DB_PATH = os.path.join(DATA_DIR, "static.db")

static_problem_set_repo: StaticProblemSetSQLiteRepository = None
static_problem_repo: StaticProblemSQLiteRepository = None
# static_answer_page_repo: StaticAnswerPageSQLiteRepository = None

db: sql.engine = None
db_meta: sql.MetaData = None

Session: sql.orm.sessionmaker = scoped_session(sessionmaker())


def initialize(db_path: str = None):
    global db, db_meta, Session
    db_path = db_path if db_path is not None else DB_PATH

    db_parent_dir = os.path.realpath(os.path.join(db_path, os.path.pardir))

    if not os.path.exists(db_parent_dir):
        os.makedirs(db_parent_dir)


    # TODO see if I can get rid of this call because SQLAlchemy handles it
    # sqlite_util.sqlite_touch(db_path)
    db = sql.create_engine(f"sqlite:///{db_path}")
    db.echo = True
    db_meta = MetaData()
    Session.configure(bind=db)
    init_repos(db)


def init_repos(engine: sql.engine.Engine):
    global static_problem_set_repo, static_problem_repo, static_answer_page_repo
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    session = Session()
    static_problem_repo = StaticProblemSQLiteRepository(session)
    static_problem_set_repo = StaticProblemSetSQLiteRepository(session)
    # static_answer_page_repo = StaticAnswerPageSQLiteRepository(conn)
