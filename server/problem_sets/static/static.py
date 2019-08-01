#  Copyright (c) 2019 Thomas Howe

from problem_sets.environment import Environment
from problem_sets.static.data import data_manager
from problem_sets.static.data.static_problem_data_source import StaticProblemDataSource
from problem_sets.static.data.static_problem_entity import StaticProblemEntity
from problem_sets.static.data.static_problem_set_data_source import StaticProblemSetDataSource
from problem_sets.static.static_problem import StaticProblem
from problem_sets.static.static_problem_set import StaticProblemSet

static_problem_data_source: StaticProblemDataSource = None
static_problem_set_data_source: StaticProblemSetDataSource = None


def static_problem(set_id: str):
    static_problem_entity: StaticProblemEntity = static_problem_data_source.pick_problem_from_set(set_id)

    static_problem: StaticProblem = StaticProblem(static_problem_entity.set_id, static_problem_entity.id,
                                                  static_problem_entity.used, static_problem_entity.content)

    return static_problem


def static_sets():
    pass
    # also for now
    # should call impl of StaticProblemSetDataSource.list()


def create_static_problem_set(set: StaticProblemSet):
    if not static_problem_set_data_source.check_id_available(set.id):
        raise Exception("ID for problem set isn't unique")

    static_problem_set_data_source.create(set)


def get_static_problem_set(id: str) -> StaticProblemSet:
    if static_problem_set_data_source.check_id_available(id):
        raise Exception(f"No static problem set for id {id}")

    return static_problem_set_data_source.get(id)


def create_problem(problem: StaticProblemEntity):
    static_problem_data_source.create(problem)


def initialize(env: Environment):
    global static_problem_data_source, static_problem_set_data_source
    data_manager.initialize()

    static_problem_data_source = data_manager.static_problem_repo
    static_problem_set_data_source = data_manager.static_problem_set_repo
