#  Copyright (c) 2019 Thomas Howe
from typing import List

from problem_sets.environment import Environment
from problem_sets.static.data import data_manager
from problem_sets.static.data.sqlite import sqlite_manager
from problem_sets.static.data.static_problem_data_source import StaticProblemDataSource
from problem_sets.static.data.static_problem_entity import StaticProblemEntity
from problem_sets.static.data.static_problem_set_data_source import StaticProblemSetDataSource
from problem_sets.static.data.static_problem_set_entity import StaticProblemSetEntity
from problem_sets.static.static_problem import StaticProblem
from problem_sets.static.static_problem_set import StaticProblemSet

static_problem_data_source: StaticProblemDataSource = None
static_problem_set_data_source: StaticProblemSetDataSource = None


def static_problem(set_id: str):
    static_problem_entity: StaticProblemEntity = static_problem_data_source.pick_problem_from_set(set_id)

    if static_problem_entity is None:
        return None

    static_problem: StaticProblem = StaticProblem(static_problem_entity.set_id, static_problem_entity.id,
                                                  static_problem_entity.used, static_problem_entity.content)

    return static_problem


def create_static_problem_set(set: StaticProblemSet):
    if not static_problem_set_data_source.check_id_available(set.id):
        raise Exception("ID for problem set isn't unique")

    static_problem_set_data_source.create(set)


def static_problem_set(id: str) -> StaticProblemSet:
    if static_problem_set_data_source.check_id_available(id):
        raise Exception(f"No static problem set for id {id}")

    static_problem_set_entity: StaticProblemSetEntity = static_problem_set_data_source.get(id)

    return StaticProblemSet(static_problem_set_entity.id, static_problem_set_entity.source,
                            static_problem_set_entity.instruction_contents, static_problem_set_entity.answer_contents)


def delete_static_problem_set(id: str) -> bool:
    if static_problem_set_data_source.check_id_available(id):
        # We didn't delete it, but we'll take credit for it
        # TODO Make an actual error response system
        return True

    return static_problem_set_data_source.delete(id)


def static_sets() -> List[StaticProblemSet]:
    static_problem_set_entities = static_problem_set_data_source.list()

    static_problem_sets = list(StaticProblemSet(entity.id, entity.source,
                                                entity.instruction_contents, entity.answer_contents) for entity in
                               static_problem_set_entities)

    return static_problem_sets


def create_problem(problem: StaticProblemEntity):
    static_problem_data_source.create(problem)


def mark_static_problem_used(id: int, used: bool):
    static_problem_data_source.set_used(id, used)


def cleanup():
    sqlite_manager.Session.remove()


def initialize(env: Environment):
    global static_problem_data_source, static_problem_set_data_source
    data_manager.initialize(env)

    static_problem_data_source = data_manager.static_problem_repo
    static_problem_set_data_source = data_manager.static_problem_set_repo
