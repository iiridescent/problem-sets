#%%

from IPython.lib.deepreload import reload
# %load_ext autoreload

from IPython.display import Latex, Markdown
from numpy import round
from math import ceil, e


#%%
# %autoreload 2

import os
# sys.path.insert(0, )

from numpy.random import choice, randint

from problem import Problem
from testbed_utils import render_debug_problem
from util import fmath, mfrac, fprice
from widget import TextWidgetOptions, Widget

p = 50 * randint(1, 21)

compounding_choices = {1: "annually", 4: "quarterly", 12: "monthly", 356: "daily"}

n_choices = list(compounding_choices.keys())

n = choice(n_choices)

t = randint(1, 3) + choice([0, 0.5])

r = randint(1, 15) / 100

a = round(p * (1 + r / n) ** (n * t), 2)

plural_end = "s" if t != 1 else ""

problem_instruction = "Find the amount that results from the following investment:"

problem_text = rf"$\${p}$ invested at ${int(r*100)}\%$ compounded {compounding_choices[n]} after a period of ${mfrac(t)}$ year{plural_end}"

solution_text = rf"$\${a}$"

content = [
    Widget(TextWidgetOptions(problem_instruction)),
    Widget(TextWidgetOptions(problem_text)),
]

solution = Widget(TextWidgetOptions(solution_text))

problem = Problem(content, [solution])

render_debug_problem(problem)
#%%


def compound_interest_find_p():
    from math import e

    a = 50 * randint(1, 21)

    compounding_choices = {1: "annually", 4: "quarterly", 12: "monthly", 356: "daily"}

    n_choices = list(compounding_choices.keys())

    n = choice(n_choices)

    t = randint(1, 3) + choice([0, 0.5])

    r = randint(1, 15) / 100

    p = round(a * (1 + r / n) ** -(n * t), 2)

    plural_end = "s" if t != 1 else ""

    problem_instruction = "Find the _present value_ of this investment:"

    problem_text = rf"To get $\${a}$ after ${mixed_fraction_string(t)}$ year{plural_end} at ${int(r*100)}\%$ compounded {compounding_choices[n]}"

    solution_text = rf"$\${p}$"

    content = [
        Widget(TextWidgetOptions(problem_instruction)),
        Widget(TextWidgetOptions(problem_text)),
    ]

    solution = Widget(TextWidgetOptions(solution_text))

    return Problem(content, [solution])


render_debug_problem(compound_interest_find_p())
#%%
# %autoreload 2


# USE THE VERSION OF THIS IN UTIL.PY INSTEAD
def format_currency_latex(input):
    if int(input) == input:
        value = str(int(input))
    else:
        value = r"{:20,.2f}".format(input)

    return f"\${value.strip()}"


def compound_interest_continuous_find_p():
    from math import e

    a = 50 * randint(1, 21)

    t = randint(1, 3) + choice([0, 0.5])

    r = randint(1, 15) / 100

    p = round(a / (e ** (t * r)), 2)

    plural_end = "s" if t != 1 else ""

    rate_str = rf"{int(r*100)}\%"

    problem_instruction = "Find the _present value_ of this investment:"

    problem_text = rf"To get {fmath(format_currency_latex(a))} after {fmath(mixed_fraction_string(t))} year{plural_end} at {fmath(rate_str)} compounded continuously"

    solution_text = rf"${format_currency_latex(p)}$"

    content = [
        Widget(TextWidgetOptions(problem_instruction)),
        Widget(TextWidgetOptions(problem_text)),
    ]

    solution = Widget(TextWidgetOptions(solution_text))

    return Problem(content, [solution])


render_debug_problem(compound_interest_continuous_find_p())

#%%


def compound_interest_discrete_find_effective_roi():
    compounding_choices = {1: "annually", 4: "quarterly", 12: "monthly", 356: "daily"}

    n_choices = list(compounding_choices.keys())

    n = choice(n_choices)

    r = randint(1, 15) / 100

    r_str = rf"{int(r*100)}\%"

    r_e = ((1 + r / n) ** (n)) - 1

    r_e_str = rf"{round(r_e*100,3)}\%"

    problem_instruction = "Find the effective return on investment for this investment (round to 3 decimal points):"

    problem_text = rf"For {fmath(r_str)} compounded {compounding_choices[n]}"

    solution_text = fmath(r_e_str)

    content = [
        Widget(TextWidgetOptions(problem_instruction)),
        Widget(TextWidgetOptions(problem_text)),
    ]

    solution = Widget(TextWidgetOptions(solution_text))

    return Problem(content, [solution])


render_debug_problem(compound_interest_discrete_find_effective_roi())

#%%


def compound_interest_continuous_find_effective_roi():
    r = randint(1, 15) / 100

    r_str = rf"{int(r*100)}\%"

    r_e = (e ** r) - 1

    r_e_str = rf"{round(r_e*100,3)}\%"

    problem_instruction = "Find the effective return on investment for this investment (round to 3 decimal points):"

    problem_text = rf"For {fmath(r_str)} compounded continuously"

    solution_text = fmath(r_e_str)

    content = [
        Widget(TextWidgetOptions(problem_instruction)),
        Widget(TextWidgetOptions(problem_text)),
    ]

    solution = Widget(TextWidgetOptions(solution_text))

    return Problem(content, [solution])


render_debug_problem(compound_interest_continuous_find_effective_roi())

#%%


def int_if_whole(input):
    if int(input) == input:
        return int(input)
    return input


def format_percent(input, decimal_points=3, mixed_fraction=False):
    value = int_if_whole(round(input * 100, 3))

    if mixed_fraction:
        value = mixed_fraction_string(value)

    return rf"{value}\%"


from numpy import linspace
from random import sample, getrandbits


def compound_interest_compare_discrete_vs_discrete():

    n_choices = list(compounding_choices.keys())

    n_1, n_2 = sample(n_choices, 2)

    # The way this works is that we come up with an interest rate for the highest compounding rate
    # then we come up with an interest rate that is some amount higher for the lower compounding rate
    # this way it's not dead easy to tell which is the better deal--and that's the point

    base_rate = randint(1, 15) / 100

    higher_rate = base_rate + choice(linspace(0.1, 0.3, 9)) / 100

    # The lower interest rate with the higher compounding rate should be fractional as
    # often as the other interest rate

    if bool(getrandbits(1)):
        old_base_rate = base_rate
        base_rate -= higher_rate - base_rate
        higher_rate = old_base_rate

    if n_1 > n_2:
        r_1 = base_rate
        r_2 = higher_rate
    else:
        r_1 = higher_rate
        r_2 = base_rate

    r_e_1 = ((1 + (r_1 / n_1)) ** n_1) - 1

    r_e_2 = ((1 + (r_2 / n_2)) ** n_2) - 1

    r_n_description_1 = (
        f"{fmath(format_percent(r_1,))} compounded {compounding_choices[n_1]}"
    )

    r_n_description_2 = (
        f"{fmath(format_percent(r_2,))} compounded {compounding_choices[n_2]}"
    )

    solution_description = r_n_description_1 if r_e_1 > r_e_2 else r_n_description_2

    problem_instruction = "Which of the following is a better investment?"

    description_set = [r_n_description_1, r_n_description_2]

    # Randomize the order
    if bool(getrandbits(1)):
        description_set = description_set.reverse()

    problem_text = f"{r_n_description_1} or {r_n_description_2}"

    solution_text = solution_description

    content = [
        Widget(TextWidgetOptions(problem_instruction)),
        Widget(TextWidgetOptions(problem_text)),
    ]

    solution = Widget(TextWidgetOptions(solution_text))

    return Problem(content, [solution])


render_debug_problem(compound_interest_compare_discrete_vs_discrete())
