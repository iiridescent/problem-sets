import os

from problem_sets.dir_util import ROOT_DIR
from problem_sets.environment import Environment

DATA_DIR = os.path.join(ROOT_DIR, "static_data")

IMAGES_DIR = os.path.join(DATA_DIR, "images")

from problem_sets.static.data.sqlite import sqlite_manager
from problem_sets.static.data.static_problem_repository import StaticProblemRepository
from problem_sets.static.data.static_problem_set_repository import StaticProblemSetRepository

static_problem_set_repo: StaticProblemSetRepository = None
static_problem_repo: StaticProblemRepository = None


# static_answer_page_repo: StaticAnswerPageRepository = None


def initialize(env: Environment):
    global static_problem_set_repo, static_problem_repo
    sqlite_manager.initialize(env)

    static_problem_set_repo = StaticProblemSetRepository(sqlite_manager.static_problem_set_repo)
    static_problem_repo = StaticProblemRepository(sqlite_manager.static_problem_repo)
