#  Copyright (c) 2019 Thomas Howe

import pytest

from problem_sets.static.data import data_manager
from problem_sets.static.data.sqlite import sqlite_manager, sqlite_util
from problem_sets.static.data.sqlite.test.sqlite_test_util import drop_tables_list
from problem_sets.static.data.static_content_entity import StaticContentEntity, StaticContentEntityType
from problem_sets.static.data.static_problem_entity import StaticProblemEntity
from problem_sets.static.data.static_problem_set_entity import StaticProblemSetEntity
from problem_sets.static.data.test import data_test_util

EXAMPLE_SET_ID = "test_id"


@pytest.fixture
def problem_set_entity():
    instruction_contents = [
        StaticContentEntity(StaticContentEntityType.text, "instruction1"),
        StaticContentEntity(StaticContentEntityType.text, "instruction2"),
        StaticContentEntity(StaticContentEntityType.text, "instruction3"),
    ]

    answer_contents = [
        StaticContentEntity(StaticContentEntityType.text, "answer1"),
        StaticContentEntity(StaticContentEntityType.text, "answer2"),
        StaticContentEntity(StaticContentEntityType.text, "answer3"),
    ]

    return StaticProblemSetEntity(EXAMPLE_SET_ID, "example source", instruction_contents, answer_contents)


@pytest.fixture
def problem_entity():
    content = [
        StaticContentEntity(StaticContentEntityType.text, "question-part-1"),
        StaticContentEntity(StaticContentEntityType.text, "question-part-2"),
        StaticContentEntity(StaticContentEntityType.text, "question-part-3"),
    ]

    return StaticProblemEntity(EXAMPLE_SET_ID, False, content, 1)


def add_problem_set_and_problem_to_db(problem_set_entity, problem_entity):
    data_manager.static_problem_set_repo.create(problem_set_entity)
    data_manager.static_problem_repo.create(problem_entity)


def test_add_problem(problem_set_entity, problem_entity):
    data_test_util.clean_start(drop_tables_list)

    add_problem_set_and_problem_to_db(problem_set_entity, problem_entity)

    command_problem_list = f"""SELECT * FROM problem WHERE set_id=? 
    """

    from problem_sets.static.data.sqlite.test.sqlite_test_util import conn

    result = sqlite_util.query_fetch(conn, command_problem_list, (EXAMPLE_SET_ID,))

    assert len(result) == 1


def test_get_problem(problem_set_entity, problem_entity):
    data_test_util.clean_start(drop_tables_list)

    add_problem_set_and_problem_to_db(problem_set_entity, problem_entity)

    result = sqlite_manager.static_problem_repo.get(problem_entity.id)

    mismatch = problem_entity

    mismatch.id = 2

    bad_result = sqlite_manager.static_problem_repo.get(mismatch.id)

    assert isinstance(result, StaticProblemEntity)
    assert bad_result is None
