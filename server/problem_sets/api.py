#  Copyright (c) 2019 Thomas Howe

from problem_sets import gen
from problem_sets import static
from problem_sets.environment import Environment

env = Environment.prod


def problem(set_id: str):
    """
    Attempt to produce a problem from set with id; first generated, then static.
    """

    # first try to generate a problem
    problem = gen.gen_problem(set_id)

    if problem is not None:
        return problem

    # didn't work, try to find a problem in static set with id 'set_id'

    problem = static.static_problem(set_id)

    # return it even if it is none, there are no available gen sets, static sets, and/or unused problems
    return problem


def sets():
    """
    Return list of all available generated (virtual) and static sets
    """
    # Will do this later, low priority
    raise NotImplementedError("'sets' hasn't been implemented")


def initialize(environment=Environment.prod):
    global env
    env = environment

    # load generated types
    gen.initialize_gen(env)
    static.initialize(env)
