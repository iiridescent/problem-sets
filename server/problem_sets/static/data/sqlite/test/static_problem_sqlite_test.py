#  Copyright (c) 2019 Thomas Howe

import pytest

from problem_sets.static.data.sqlite import sqlite_manager, sqlite_util
from problem_sets.static.data.sqlite.static_problem_set_sqlite_repository import PROBLEM_SETS_TABLE_ID
from problem_sets.static.data.sqlite.static_problem_sqlite_repository import PROBLEMS_TABLE_ID
from problem_sets.static.data.sqlite.test import sqlite_test_util
from problem_sets.static.static_problem_entity import StaticProblemEntity
from problem_sets.static.static_problem_set_entity import StaticProblemSetEntity

EXAMPLE_SET_ID = "test_id"


@pytest.fixture()
def problem_set_entity():
    return StaticProblemSetEntity(EXAMPLE_SET_ID, "example source")


@pytest.fixture
def problem_entity():
    return StaticProblemEntity(1, set_id=EXAMPLE_SET_ID, used=False)


def add_problem_set_and_problem_to_db(problem_set_entity, problem_entity):
    sqlite_manager.static_problem_set_repo.create(problem_set_entity)

    sqlite_manager.static_problem_repo.create(problem_entity)


def test_add_problem(problem_set_entity, problem_entity):
    sqlite_test_util.clean_start([PROBLEMS_TABLE_ID, PROBLEM_SETS_TABLE_ID])

    add_problem_set_and_problem_to_db(problem_set_entity, problem_entity)

    command_problem_list = f"""SELECT * FROM problems WHERE set_id=? 
    """

    result = sqlite_util.query_fetch(sqlite_manager.conn, command_problem_list, (EXAMPLE_SET_ID,))

    assert len(result) == 1


def test_get_problem(problem_set_entity, problem_entity):
    sqlite_test_util.clean_start([PROBLEMS_TABLE_ID, PROBLEM_SETS_TABLE_ID])

    add_problem_set_and_problem_to_db(problem_set_entity, problem_entity)

    result = sqlite_manager.static_problem_repo.get(problem_entity.id)

    mismatch = StaticProblemEntity(id=2)

    bad_result = sqlite_manager.static_problem_repo.get(mismatch.id)

    assert isinstance(result, StaticProblemEntity)
    assert bad_result is None
