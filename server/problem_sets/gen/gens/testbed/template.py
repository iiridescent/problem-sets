#%%

# Import all of this

from IPython.lib.deepreload import reload

#%load_ext autoreload

from IPython.display import Latex, Markdown

from problem_sets import (
    fexpprod,
    froot,
    ffrac,
    fper,
    fmath,
    fcur,
    render_latex,
    render_testbed_problem,
    DebugProblemWrapper,
    create_full_text_problem,
    debug,
    gen,
    Environment,
)
from sympy import Expr, symbols, latex
from numpy import arccos, arcsin, arctan, around
from numpy.random import randint, choice, seed
from numbers import Number
from enum import Enum
from fractions import Fraction

#%%
# %autoreload 2


@debug
# Problem type decorator (don't uncomment this until it's ready to be tested on the server, because the server will import it):
@gen(
    description="Example problem type",
    source="Example source",
    target_env=Environment.debug,
)
def example_testbed_problem_type():
    problem_instruction = "Example problem instruction:"

    problem_text = "Example problem content."
    solution_text = "Example problem solution."

    debug_info = [{"example debug info": None}]

    return create_full_text_problem(
        [problem_instruction, problem_text], [solution_text], debug_info
    )
