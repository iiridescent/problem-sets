#%%

#%load_ext autoreload
# %autoreload 2

from problem_sets import (
    fmath,
    fexpprod,
    ffrac,
    fsign,
    froot,
    fbra,
    ftrigfun,
    LatexTrigFunction,
    randint_gap_tuple,
    sign,
    Problem,
    create_full_text_problem,
    problem_type,
    render_testbed_problem,
    pick_from_list,
    debug
)
from numpy import arccos, arcsin, arctan, around
from numpy.random import randint, choice
from fractions import Fraction

#%%

@debug
@problem_type(source="Sullivan Trigonometry 3.2, 35-56", debug=True)
def find_trig_func_arc_inverse_with_calculator():
    problem_instruction = "Use a calculator to find the value of this expression rounded to two decimal places:"

    # schema: latex insert (superscript -1 is added for all of them), function, whether or not there's a gap from -1 to 1
    functions = [
        (LatexTrigFunction.arccsc, lambda x: arcsin(1 / x), True),
        (LatexTrigFunction.arcsec, lambda x: arccos(1 / x), True),
        (LatexTrigFunction.arccot, lambda x: arctan(1 / x), False),
    ]

    picked_function = pick_from_list(functions, 1)

    picked_function_has_gap = picked_function[2]

    number_types = ["fraction", "sqrt", "whole"]
    picked_number_type = pick_from_list(number_types)

    picked_number = None

    domain_gap = (-1, 1)

    fraction_range = (-4, 4)
    sqrt_range = [2, 3, 5, 6, 7, 8, 10]
    whole_range = (-10, 10)

    def pick_number():
        if picked_number_type == "fraction":
            # denominator shouldn't be 1
            denominator = randint_gap_tuple(fraction_range, (-2, 2))

            denominator_sign = sign(denominator)

            numerator_sign = choice([denominator_sign, -denominator_sign])

            if picked_function_has_gap:
                numerator = numerator_sign * (abs(denominator) + 1)
            else:
                numerator = numerator_sign * (abs(denominator) + choice([-1, 1]))

            fraction = Fraction(numerator, denominator).limit_denominator()
            # simplify
            numerator = fraction.numerator
            denominator = fraction.denominator

            # fraction_sign = "" if fraction >= 0 else "-"

            return (
                numerator / denominator,
                ffrac((numerator, denominator), mixed=False),
            )
        elif picked_number_type == "sqrt":
            square = choice(sqrt_range)
            return (square, froot(square))
        elif picked_number_type == "whole":
            whole_number = randint_gap_tuple(whole_range, domain_gap)
            return (whole_number, str(whole_number))

    picked_number = pick_number()

    answer = around(picked_function[1](picked_number[0]), 2)

    problem_text = fmath(
        ftrigfun(
            fbra(picked_number[1], tall=(picked_number_type == "fraction")),
            picked_function[0],
        )
    )
    solution_text = fmath(answer)

    debug_info = [
        {"picked_number_type": picked_number_type},
        {"picked_function": "arc" + picked_function[0].value},
        {"picked number": picked_number[1]},
    ]

    return create_full_text_problem(
        [problem_instruction, problem_text], solution_text, debug_info
    )
