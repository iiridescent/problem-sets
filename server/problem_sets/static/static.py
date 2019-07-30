#  Copyright (c) 2019 Thomas Howe

from problem_sets.environment import Environment
from problem_sets.static.data.sqlite import sqlite_manager
from problem_sets.static.data.static_answer_page_data_source import StaticAnswerPageDataSource
from problem_sets.static.data.static_problem_data_source import StaticProblemDataSource
from problem_sets.static.data.static_problem_set_data_source import StaticProblemSetDataSource

static_problem_repo: StaticProblemDataSource = None
static_problem_set_data_source: StaticProblemSetDataSource = None
static_answer_page_data_source: StaticAnswerPageDataSource = None


def problem(set_id: str):
    return static_problem_repo.get(set_id)


def sets():
    pass
    # also for now
    # should call impl of StaticProblemSetDataSource.list()


def initialize(env: Environment):
    global static_problem_repo
    sqlite_manager.initialize()

    static_problem_data_source = sqlite_manager.static_problem_repo
