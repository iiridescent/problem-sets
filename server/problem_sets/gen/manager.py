#  Copyright (c) 2019 Thomas Howe

import importlib
import os
from dataclasses import dataclass
from numbers import Number
from types import FunctionType

from numpy import int64
from numpy.random import seed as np_seed, randint

from problem_sets.environment import Environment
from problem_sets.gen.gen_problem import GenProblemContent, GenProblem

GEN_PATH = "problem_sets.gen"

GENS = "gens"

registered_gens = {}

# default environment is production
env = Environment.prod


@dataclass
class Gen:
    """
    Class for storing problem type attributes
    """

    fun: FunctionType
    set_id: str
    description: str
    source: str
    # If true, this gen will only be available when the global environment is debug
    target_env: Environment

    def serialize(self):
        return {
            "set_id": self.set_id,
            "fun": self.fun,
            "description": self.description,
            "source": self.source,
            "target_env": self.target_env,
        }


def gen_def(name=None, description=None, source=None, target_env=Environment.prod):
    """
    Annotation for registering problem generator
    """

    def inner(fun: FunctionType):
        nonlocal name
        name = name if name is not None else fun.__name__.replace("_", "-")

        def wrapper(random_seed: Number = None):
            # upper bound of Numpy seed is 2**32 - 1
            random_seed = random_seed if random_seed else randint(0, 2 ** 32 - 1, dtype=int64)

            # convert to int so it can be serialized
            random_seed = int(random_seed)

            np_seed()

            problem_content: GenProblemContent = fun()
            problem = GenProblem.from_content(problem_content, name, random_seed)

            return problem

        loaded_gen = Gen(wrapper, name, description, source, target_env)

        if target_env == env:
            register_gen(loaded_gen)

        return wrapper

    return inner


def register_gen(problem_type: Gen):
    """
    Add problem generator to registry
    """

    print(f"Loaded gen {problem_type.set_id}")

    registered_gens[problem_type.set_id] = problem_type


def gen_paths():
    """
    :return: list of paths for problem generators
    """
    problem_directories = []
    for d in os.listdir(gens_path()):
        path = gens_path(d)
        if not os.path.exists(os.path.join(path, "__init__.py")):
            continue
        problem_directories.append(d)

    problem_directories.sort()

    return problem_directories


def load_gens(environment: Environment = Environment.prod):
    global env
    env = environment

    gens = gen_paths()

    loaded_gens = []

    for gen_source in gens:
        package = f"{GEN_PATH}.{GENS}.{gen_source}"

        try:
            loaded_type = importlib.import_module(package)
            loaded_gens.append(loaded_type)
            print(f"Loaded problem generator {gen_source}")
        except ImportError as e:
            # fail gracefully
            print(f"Generator {gen_source} failed to load with error:\n{e}")


def gens_path(dir: str = None):
    """
    Get base directory for problem generators
    :param dir:
    :return:
    """
    pwd = os.path.dirname(os.path.realpath(__file__))

    problems_path = os.path.join(pwd, GENS)

    if not dir:
        return problems_path

    return os.path.join(problems_path, dir)
