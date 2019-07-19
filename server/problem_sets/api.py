from problem_sets import manager
from problem_sets.environment import Environment

env = Environment.prod


def generate_problem(type_ref: str):
    return manager.registered_problem_types[type_ref].fun()


def initialize(environment=Environment.prod):
    global env
    env = environment

    manager.load_types(environment)
