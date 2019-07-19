#%%

# Import all of this

from IPython.lib.deepreload import reload

#%load_ext autoreload

from IPython.display import Latex, Markdown

from util import fexpprod, froot, ffrac, fper, fmath, fcur
from sympy import Expr, symbols, latex
from numpy import arccos, arcsin, arctan, around
from numpy.random import randint, choice
from numbers import Number
from testbed_utils import render_latex, render_testbed_problem, DebugProblemWrapper
from enum import Enum
from environment import Environment
from problem import create_full_text_problem
from problem_type_manager import problem_type
from fractions import Fraction

#%%
# %autoreload 2

# Problem type decorator (don't uncomment this until it's ready to be tested on the server, because the server will import it):
# @problem_type(description="Example problem type", source="Example source")
def example_testbed_problem_type():
    problem_instruction = "Example problem instruction:"

    problem_text = "Example problem content"
    solution_text = "Example problem solution"

    debug_info = [
        {"example debug info": None},
    ]

    return create_full_text_problem(
        [problem_instruction, problem_text], [solution_text], debug_info
    )

render_testbed_problem(example_testbed_problem_type)