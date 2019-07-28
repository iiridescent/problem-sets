from problem_sets.gen.manager import registered_gens, load_gens
from problem_sets.environment import Environment


def problem(set_id: str):
    """
    Attempt to generate problem with generator id 'set_id' (generators have an infinite virtual "set")
    """
    return registered_gens[set_id].fun()


def sets():
    """
    List of names of all available problem generators
    """
    return registered_gens.keys()


def initialize(env: Environment):
    load_gens(env)
