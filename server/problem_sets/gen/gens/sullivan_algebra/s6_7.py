from math import e
from random import getrandbits, sample

from numpy import linspace
from numpy.random import choice, randint

from problem_sets import (
    Problem,
    create_full_text_problem,
    gen,
    render_testbed_problem,
    fcur,
    fmath,
    fper,
    iiw,
    ffrac,
    fplural,
    TextWidgetOptions,
    Widget,
)
from numbers import Number

compounding_choices = {
    1: "annually",
    2: "semiannually",
    4: "quarterly",
    12: "monthly",
    356: "daily",
}

compounding_n_choices = list(compounding_choices.keys())


@gen(
    description="Find the amount $A$ that results from an investment that compounds discretely.",
    source="Sullivan Algebra 6.7 7-14",
)
def compound_interest_discrete_find_a():
    p = 50 * randint(1, 21)

    n = choice(compounding_n_choices)

    t = randint(1, 3) + choice([0, 0.5])

    r = randint(1, 15) / 100

    a = f_compound_interest_discrete(p, r, n, t)

    year_word = fplural("year", "years", t)

    problem_instruction = "Find the amount that results from this following investment:"

    problem_text = f"{fmath(fcur(p))} invested at {fmath(fcur(r))} compounded {compounding_choices[n]} after a period of {fmath(ffrac(t))} {year_word}"

    solution_text = fmath(fcur(a))

    return create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )


@gen(
    description="Find the present value (principal) $P$ of an investment that compounds discretely.",
    source="Sullivan Algebra 6.7 15-20",
)
def compound_interest_discrete_find_p():
    a = 50 * randint(1, 21)

    n = choice(compounding_n_choices)

    t = randint(1, 3) + choice([0, 0.5])

    r = randint(1, 15) / 100

    p = round(f_present_value_discrete(a, r, n, t), 2)

    year_word = fplural("year", "years", t)

    problem_instruction = "Find the present value of this investment:"

    problem_text = f"To get {fmath(fcur(a))} after {fmath(ffrac(t))} {year_word} at {fmath(fper(r))} compounded {compounding_choices[n]}"

    solution_text = fmath(fcur(p))

    return create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )


@gen(
    description="Find the present value (principal) $p$ of an investment that compounds continuously.",
    source="Sullivan Algebra 6.7 21-22",
)
def compound_interest_continuous_find_p():

    a = 50 * randint(1, 21)

    t = randint(1, 3) + choice([0, 0.5])

    r = randint(1, 15) / 100

    p = round(f_present_value_continuous(a, r, t), 2)

    plural_end = "s" if t != 1 else ""

    problem_instruction = "Find the present value of this investment:"

    problem_text = f"To get {fmath(fcur(a))} after {fmath(ffrac(t))} year{plural_end} at {fmath(fper(r))} compounded continuously"

    solution_text = fmath(fcur(p))

    return create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )


@gen(
    description="Find the effective return on investment $r_e$ of an investment that compounds discretely.",
    source="Sullivan Algebra 6.7 23-24",
)
def compound_interest_discrete_find_effective_roi():
    n = choice(compounding_n_choices)

    r = randint(1, 15) / 100

    r_e = f_effective_rate_of_interest_discrete(r, n)

    problem_instruction = "Find the effective return on investment for this investment (round to 3 decimal points):"

    problem_text = f"For {fmath(fper(r))} compounded {compounding_choices[n]}"

    solution_text = fmath(fper(r_e))

    return create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )


@gen(
    description="Find the effective return on investment $r_e$ of an investment that compounds continuously.",
    source="Sullivan Algebra 6.7 25-26",
)
def compound_interest_continuous_find_effective_roi():
    r = randint(1, 15) / 100

    r_e = f_effective_rate_of_interest_continuous(r)

    problem_instruction = "Find the effective return on investment for this investment (round to 3 decimal points):"

    problem_text = f"For {fmath(fper(r))} compounded continuously"

    solution_text = fmath(fper(r_e))

    return create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )


@gen(
    description="Find the highest effective interest rate between two investments that compound discretely.",
    source="Sullivan Algebra 6.7 27-30",
)
def compound_interest_compare_discrete_vs_discrete():
    n_1, n_2 = sample(compounding_n_choices, 2)

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

    r_e_1 = f_effective_rate_of_interest_discrete(r_1, n_1)

    r_e_2 = f_effective_rate_of_interest_discrete(r_1, n_1)

    r_n_description_1 = f"{fmath(fper(r_1,))} compounded {compounding_choices[n_1]}"

    r_n_description_2 = f"{fmath(fper(r_2,))} compounded {compounding_choices[n_2]}"

    solution_description = r_n_description_1 if r_e_1 > r_e_2 else r_n_description_2

    problem_instruction = "Which of the following is a better investment?"

    description_set = [r_n_description_1, r_n_description_2]

    # Randomize the order
    if bool(getrandbits(1)):
        description_set = description_set.reverse()

    problem_text = f"{r_n_description_1} or {r_n_description_2}"

    solution_text = solution_description

    return create_full_text_problem(
        [problem_instruction, problem_text], [solution_text]
    )


def f_compound_interest_discrete(p: Number, r: Number, n: Number, t: Number = 1):
    return p * (1 + (r / n)) ** (n * t)


def f_compound_interest_continuous(p: Number, r: Number, t: Number = 1):
    return p * e ** (r * t)


def f_effective_rate_of_interest_discrete(r: Number, n: Number, t: Number = 1):
    return ((1 + (r / n)) ** (n * t)) - 1


def f_effective_rate_of_interest_continuous(r: Number, t: Number = 1):
    return (e ** (r * t)) - 1


def f_present_value_discrete(a: Number, r: Number, n: Number, t: Number = 1):
    return a * (1 + (r / n)) ** (-n * t)


def f_present_value_continuous(a: Number, r: Number, t: Number = 1):
    return a * e ** (-r * t)
