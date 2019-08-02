#  Copyright (c) 2019 Thomas Howe

import os

import sqlalchemy as sql
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from problem_sets.environment import Environment

Base = declarative_base()

# Base must be created before these are imported
from problem_sets.static.data.data_manager import DATA_DIR
from problem_sets.static.data.sqlite.static_content_sqlite_repository import StaticContentSQLiteRepository
from problem_sets.static.data.sqlite.static_problem_sqlite_repository import StaticProblemSQLiteRepository
from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import StaticProblemSetSQLiteRepository

DB_PATH = os.path.join(DATA_DIR, "static.db")

static_content_repo: StaticContentSQLiteRepository = None
static_problem_set_repo: StaticProblemSetSQLiteRepository = None
static_problem_repo: StaticProblemSQLiteRepository = None

db: sql.engine = None
db_meta: sql.MetaData = None

Session: scoped_session = scoped_session(sessionmaker())


def initialize(env: Environment, db_path: str = None):
    global db, db_meta, Session
    db_path = db_path if db_path is not None else DB_PATH

    db_parent_dir = os.path.realpath(os.path.join(db_path, os.path.pardir))

    if not os.path.exists(db_parent_dir):
        os.makedirs(db_parent_dir)

    db = sql.create_engine(f"sqlite:///{db_path}")
    db.echo = env == Environment.debug
    db_meta = MetaData()
    Session.configure(bind=db)
    init_repos(db)


def init_repos(engine: sql.engine.Engine):
    global static_content_repo, static_problem_set_repo, static_problem_repo
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    static_content_repo = StaticContentSQLiteRepository(Session)
    static_problem_repo = StaticProblemSQLiteRepository(Session)
    static_problem_set_repo = StaticProblemSetSQLiteRepository(Session)
