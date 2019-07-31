#  Copyright (c) 2019 Thomas Howe

from problem_sets.environment import Environment
from problem_sets.static.data import data_manager
from problem_sets.static.data.sqlite import sqlite_manager
from problem_sets.static.data.static_problem_data_source import StaticProblemDataSource
from problem_sets.static.data.static_problem_set_data_source import StaticProblemSetDataSource

static_problem_repo: StaticProblemDataSource = None
static_problem_set_data_source: StaticProblemSetDataSource = None


def problem(set_id: int):
    return static_problem_repo.get(set_id)


def sets():
    pass
    # also for now
    # should call impl of StaticProblemSetDataSource.list()


def initialize(env: Environment):
    global static_problem_repo, static_problem_set_data_source
    sqlite_manager.initialize()

    static_problem_data_source = data_manager.static_problem_repo
    static_problem_set_data_source = data_manager.static_problem_set_repo
