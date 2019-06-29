import importlib
import os
from sys import stderr
from dataclasses import dataclass
from types import FunctionType

PROBLEM_TYPES = "problem_types"

registered_problem_types = {}

@dataclass
class ProblemType:
    """ Class for storing problem type attributes """

    fun: FunctionType
    name: str
    description: str
    source: str

    def serialize(self):
        return {
            "name": self.name,
            "fun": self.fun,
            "description": self.description,
            "source": self.source,
        }


def problem_type(name=None, description=None, source=None):
    """ Annotation for registering problem """

    def inner(fun: FunctionType):
        nonlocal name
        name = name if name != None else fun.__name__.replace("_", "-")
        problem_type = ProblemType(fun, name, description, source)
        register_problem(problem_type)

    return inner


def register_problem(problem_type: ProblemType):
    """
    Add problem type to problem type registry
    """

    print(f"Loaded problem type {problem_type.name}")

    registered_problem_types[problem_type.name] = problem_type


def problem_types_paths():
    problem_directories = []
    for d in os.listdir(problems_types_path()):
        path = problems_types_path(d)
        if not os.path.exists(os.path.join(path, "__init__.py")):
            continue
        problem_directories.append(d)

    problem_directories.sort()

    return problem_directories


def load_problems():
    problem_types = problem_types_paths()

    loaded_problems_types = []

    for problem_source in problem_types:
        package = PROBLEM_TYPES + "." + problem_source

        try:
            loaded_type = importlib.import_module(package)
            loaded_problems_types.append(loaded_type)
            print(f"Loaded problem source {problem_source}")
        except ImportError as e:
            # fail gracefully
            print(f"Problem source {problem_source} failed to load with error:\n{e}")


def problems_types_path(dir: str = None):
    pwd = os.path.dirname(os.path.realpath(__file__))

    problems_path = os.path.join(pwd, PROBLEM_TYPES)

    if not dir:
        return problems_path

    return os.path.join(problems_path, dir)
