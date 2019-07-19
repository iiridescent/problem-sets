import math
from random import Random
from typing import List

from problem_sets import Problem, create_full_text_problem, problem_type, fmath, ford, Widget

@problem_type(
    description="$a$ is the sum of $n$ consecutive integers, find the $m$th",
    source="Created by Thomas Howe"
)
def sum_consecutive_integers(integer_count: bool = None, max_initial_integer: int = 50) -> Problem:
    if integer_count is not None and integer_count < 2:
        raise ValueError('parameter integer_count on sum_consecutive_integers must be greater than or equal to 2')

    integer_count = integer_count if integer_count is not None else Random().randint(3, 5)

    base_integer = Random().randrange(0, max_initial_integer)

    final_integer = 0

    for i in range(integer_count):
        final_integer += base_integer + i

    nth_integer_to_find = Random().randint(1, integer_count)

    ordinal_number = ford(nth_integer_to_find)

    question_label = f"The number {fmath(final_integer)} is the sum of {fmath(integer_count)} consecutive integers. What is the {ordinal_number}?"

    solution_integer = base_integer + (nth_integer_to_find - 1)

    solution = fmath(solution_integer)

    return create_full_text_problem([question_label], [solution])
