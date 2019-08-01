#  Copyright (c) 2019 Thomas Howe

from problem_sets.environment import Environment
from problem_sets.gen.manager import registered_gens, load_gens


def gen_problem(set_id: str):
    """
    Attempt to generate problem with generator id 'set_id' (generators have an infinite virtual "set")
    """
    if set_id not in registered_gens:
        return
    return registered_gens[set_id].fun()


def gen_sets():
    """
    List of names of all available problem generators
    """
    return registered_gens.keys()


def initialize_gen(env: Environment):
    load_gens(env)
