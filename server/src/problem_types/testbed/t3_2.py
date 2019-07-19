#%%
from IPython.lib.deepreload import reload

#%load_ext autoreload

from IPython.display import Latex, Markdown

from util import fmath
from sympy import Expr, symbols, latex
from numpy import arccos, arcsin, arctan, around
from numpy.random import randint, choice
from numbers import Number
from testbed_utils import render_latex, render_testbed_problem, DebugProblemWrapper
from enum import Enum
from environment import Environment
from problem import create_full_text_problem
from fractions import Fraction

#%%
# %autoreload 2


def find_trig_func_arc_inverse_with_calculator():
    problem_instruction = "Use a calculator to find the value of this expression rounded to two decimal places:"

    functions = {
        "arccsc": ("csc", lambda x: arcsin(1 / x), True),
        "arcsec": ("sec", lambda x: arccos(1 / x), True),
        "arccot": ("cot", lambda x: arctan(1 / x), False),
    }
    function_keys = list(functions.keys())

    picked_function_key = function_keys[randint(0, len(function_keys))]
    picked_function = functions[picked_function_key]

    picked_function_has_gap = picked_function[2]

    number_types = ["fraction", "sqrt", "whole"]
    picked_number_type = choice(number_types)

    picked_number = None

    fraction_range = (-4, 4)
    sqrt_range = (1, 10)
    whole_range = (-10, 10)

    def pick_number():
        if picked_number_type == "fraction":
            # denominator shouldn't be 1
            denominator = choice(
                [randint(fraction_range[0], -1), randint(2, fraction_range[1] + 1)]
            )
            denominator_sign = 1 if denominator >= 0 else -1
            if picked_function_has_gap:
                numerator = denominator_sign * (abs(denominator)+1)
            else:
                numerator = denominator_sign * (abs(denominator)+choice([-1, 1]))
            
            fraction = Fraction(numerator, denominator).limit_denominator()
            # simplify
            numerator = fraction.numerator
            denominator = fraction.denominator
            fraction_sign = "" if fraction >= 0 else "-"

            return (
                numerator / denominator,
                f"{fraction_sign}\\frac{{{abs(fraction.numerator)}}}{{{abs(fraction.denominator)}}}"
                if abs(denominator) != 1 and abs(numerator) != abs(denominator)
                else f"{fraction_sign}{abs(numerator)}",
            )
        elif picked_number_type == "sqrt":
            square = randint(sqrt_range[0], sqrt_range[1])
            return (square ** 0.5, f"\sqrt{{{square}}}")
        elif picked_number_type == "whole":
            whole_number = choice(
                [randint(whole_range[0], 0), randint(1, whole_range[1] + 1)]
            )
            return (whole_number, str(whole_number))

    picked_number = pick_number()

    answer = around(picked_function[1](picked_number[0]), 3)

    problem_text = fmath(f"\{picked_function[0]}^{{-1}}({picked_number[1]})")
    solution_text = fmath(str(answer))

    problem = create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )

    if env.is_debug():
        debug_info = [
            {"picked_number_type": picked_number_type},
            {"picked_function": picked_function_key},
            {"picked number": picked_number},
        ]
        return DebugProblemWrapper(debug_info, problem)

    return problem


render_testbed_problem(find_trig_func_arc_inverse_with_calculator)
