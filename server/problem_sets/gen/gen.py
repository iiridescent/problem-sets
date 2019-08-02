#  Copyright (c) 2019 Thomas Howe

from problem_sets.environment import Environment
from problem_sets.gen.manager import registered_gens, load_gens


def gen_problem(set_id: str):
    """
    Attempt to generate problem with generator id 'set_id' (generators have an infinite virtual "set")
    """

    problem_id = None

    if ':' in set_id:
        set_id_split = set_id.split(':')
        problem_id = int(set_id_split[1])
        set_id = set_id_split[0]

    if set_id not in registered_gens:
        return

    return registered_gens[set_id].fun(problem_id)


def gen_sets():
    """
    List of names of all available problem generators
    """
    return registered_gens.keys()


def initialize_gen(env: Environment):
    load_gens(env)
