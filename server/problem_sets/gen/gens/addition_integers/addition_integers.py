#  Copyright (c) 2019 Thomas Howe

import random

from problem_sets import Problem, fmath, gen_def, Widget, build_text_widget_options


@gen_def(description="Add two integers", source="Created by Thomas Howe")
def addition_integers(length=2, low=1, high=10) -> Problem:
    length = int(length)
    low = int(low)
    high = int(high)
    if length < 2:
        raise ValueError("addition problem must have length of 2")

    if low > high:
        raise ValueError("max must be greater than or equal to min")

    equation = ""
    sum = 0

    for i in range(length):
        value = random.randrange(low, high)
        equation += str(value)
        sum += value
        if i < length - 1:
            equation += "+"

    problem_value = fmath(equation)
    solution_value = "\\({}\\)".format(sum)
    problem_widget = Widget(build_text_widget_options(problem_value))
    solution_widget = Widget(build_text_widget_options(solution_value))

    return Problem([problem_widget], [solution_widget])
