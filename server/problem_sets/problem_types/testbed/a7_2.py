#%%
from IPython.lib.deepreload import reload
#%load_ext autoreload

from IPython.display import Latex, Markdown

from util import fmath
from sympy import Expr, symbols, latex
from numbers import Number
from testbed_utils import render_latex
from enum import Enum

#%%
# %autoreload 2

def f_expr_str_vert_parabola(a: Number, h: Number, k: Number):
    x, y = symbols("x y")

    coeff = 4*a

    y_k = f"{coeff}({y-k})"

    x_h = f"({x-h})"

    expr = f"{latex(x_h)}={y_k}"
    return (expr)

Latex(f_expr_str_vert_parabola(4, 2, 2))

#%%

def f_expr_str_horiz_parabola(a: Number, h: Number, k: Number):
    x, y = symbols("x y")

    coeff = 4*a

    x_h = f"({latex(x-h)})" if h != 0 else x

    y_k = f"{coeff}({(y-k)})" if h != 0 else latex(coeff*y)

    expr = f"{x_h}={latex(y_k)}"
    return expr

Latex(f_expr_str_horiz_parabola(4, -2, -2))

#%%

from enum import Enum
from numbers import Number
from sympy import symbols, latex

### IMPORT THIS FROM UTIL
class Axis(Enum):
    x = 0
    y = 1

def f_expr_str_parabola(a: Number, h: Number, k: Number, axis: Axis = Axis.x):
    x, y = symbols("x y")

    x_h = x-h

    y_k = y-k

    term_1 = x_h**2 if axis == Axis.y else y_k**2
    term_2 = y_k if axis == Axis.y else x_h

    term_1_shift = h if axis == Axis.y else k
    term_2_shift = k if axis == Axis.y else h

    coeff = 4*a

    term_1_str = term_1

    term_2_str = f"{coeff}({(term_2)})" if term_2_shift != 0 else latex(coeff*term_2)

    expr = f"{latex(term_1_str)}={latex(term_2_str)}"
    return expr



Latex(f_expr_str_parabola(2, 2, 2, Axis.x))

#%%

def f_lr_parabola(a: Number, h: Number, k: Number, axis: Axis = Axis.x):
    dependent = 4*a

Latex(f_lr_parabola(2, 2, 2, Axis.x))

#%%

from problem import create_full_text_problem
from testbed_utils import render_testbed_problem, DebugProblemWrapper
from util import fmath
from random import getrandbits
from numpy.random import randint, choice
from util import Axis
from enum import Enum
from environment import Environment

def geom_parabola_given_f_v_find_eq_and_lr(env: Environment=Environment.prod):

    problem_instruction = f"Find the equation of a parabola, and find the two points that define the latus rectum."
    
    a = choice([randint(-5, 0),randint(1, 6)])

    a_abs = abs(a)
    
    axis = choice([Axis.x, Axis.y])

    f = (0, a) if axis == Axis.y else (a, 0)

    shift = (0, 0) if bool(getrandbits(1)) else (randint(-5, 6), randint(-5, 6))

    shifted_f = tuple(map(sum,zip(f,shift)))

    problem_text = f"Focus at {fmath(str(shifted_f), env)}; vertex at {fmath(str(shift), env)}"

    expr = f_expr_str_parabola(a, shift[0], shift[1], axis)

    lr_abs = 4*

    solution_text = fmath(expr, env)

    problem = create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )

    if env.is_debug():
        debug_info = [{'a_abs': a_abs}, {"f": f}]
        return DebugProblemWrapper(debug_info, problem)

    return problem

render_testbed_problem(geom_parabola_given_f_v_find_eq_and_lr)
#%%

def geom_parabola_given_f_d_find_eq_and_lr(env: Environment=Environment.prod):

    problem_instruction = f"Find the equation of a parabola, and find the two points that define the latus rectum."
    
    a = choice([randint(-5, 0),randint(1, 6)])

    a_abs = abs(a)
    
    axis = choice([Axis.x, Axis.y])

    d = -a

    shift = (0, 0) if bool(getrandbits(1)) else (randint(-5, 6), randint(-5, 6))

    shifted_d = d + (shift[0] if axis == Axis.x else shift[1])

    d_str = f"x={shifted_d}" if axis == Axis.x else f"y={shifted_d}"

    problem_text = f"Directrix the line {fmath(d_str, env)}; vertex at {fmath(str(shift), env)}"

    expr = f_expr_str_parabola(a, shift[0], shift[1], axis)

    solution_text = fmath(expr, env)

    problem = create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )

    if env.is_debug():
        debug_info = [{'a_abs': a_abs}, {"d": d}]
        return DebugProblemWrapper(debug_info, problem)

    return problem

render_testbed_problem(geom_parabola_given_f_d_find_eq_and_lr)

#%%

def geom_parabola_given_v_aos_p_find_eq_and_lr(env: Environment=Environment.prod):

    problem_instruction = f"Find the equation of a parabola, and find the two points that define the latus rectum."
    
    a = choice([randint(-5, 0),randint(1, 6)])

    a_abs = abs(a)
    
    axis = choice([Axis.x, Axis.y])

    d = -a

    shift = (0, 0) if bool(getrandbits(1)) else (randint(-5, 6), randint(-5, 6))

    shifted_d = d + (shift[0] if axis == Axis.x else shift[1])

    d_str = f"x={shifted_d}" if axis == Axis.x else f"y={shifted_d}"

    problem_text = f"Directrix the line {fmath(d_str, env)}; vertex at {fmath(str(shift), env)}"

    expr = f_expr_str_parabola(a, shift[0], shift[1], axis)

    solution_text = fmath(expr, env)

    problem = create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )

    if env.is_debug():
        debug_info = [{'a_abs': a_abs}, {"d": d}]
        return DebugProblemWrapper(debug_info, problem)

    return problem

render_testbed_problem(geom_parabola_given_f_d_find_eq_and_lr)