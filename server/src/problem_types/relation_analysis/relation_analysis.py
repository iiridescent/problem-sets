import math
from random import Random
from typing import List

from problem import Problem

from problem_generator_manager import problem_type
from util import fmath
from widget import Widget, build_text_widget_options

# Arbitrary number to keep while loops from hanging in rare cases
MAX_RANDOM_TRIES = 50

QUESTION_IS_FUNCTION = "is_function"
QUESTION_DOMAIN = "domain"
QUESTION_RANGE = "range"

QUESTION_DOMAIN_AND_RANGE = "domain_and_range"


# {QUESTION_IS_FUNCTION: False, QUESTION_DOMAIN: False, QUESTION_RANGE: False}

def relation_analysis(question_types: List[str], is_function: bool = None, length: int = None, ) -> Problem:
    """Question types:
    - is_function
    - domain
    - range
    """

    if question_types is None:
        raise ValueError('must specify question type for relation_analysis')

    if length is not None and (length < 2 or length > 10):
        raise ValueError('length of relation must be greater than or equal to 2')

    questions = {
        QUESTION_IS_FUNCTION: 'Does this relation represent a function?',
        QUESTION_DOMAIN_AND_RANGE: "What are the domain and range of this function?",
        QUESTION_DOMAIN: 'What is the domain of this relation?',
        QUESTION_RANGE: 'What is the range of this relation?',
    }

    # problem
    is_function = is_function if is_function is not None else Random().random() < 0.5
    length = length if length is not None else Random().randrange(2, 5)

    x_values = []  # type: List[int]
    y_values = []  # type: List[int]

    def generate_neg_9_to_9_scalar() -> int:
        return Random().randrange(-9, 9)

    for i in range(length):
        if is_function and len(x_values) > 0:
            is_unique = False
            while not is_unique:
                x = generate_neg_9_to_9_scalar()
                is_unique = True
                for x2 in x_values:
                    if x == x2:
                        is_unique = False
                        break
        else:
            x = generate_neg_9_to_9_scalar()

        y = generate_neg_9_to_9_scalar()
        x_values.append(x)
        y_values.append(y)

    # We need to make sure there is at least one duplicate if this isn't a function
    if not is_function:
        has_duplicate = False
        for i in range(len(x_values) - 1):
            x = x_values[i]
            for j in range(i + 1, len(x_values)):
                x2 = x_values[j]
                if x == x2:
                    has_duplicate = True
                    break
            if has_duplicate:
                break

        if not has_duplicate:

            random_i_1 = Random().randrange(0, len(x_values))

            random_i_2 = 0
            tries = 0
            same_index = True

            while same_index and tries < MAX_RANDOM_TRIES:
                random_i_2 = Random().randrange(0, len(x_values))
                if random_i_2 != random_i_1:
                    same_index = False
                tries += 1
            if same_index:
                raise TimeoutError('attempted {} times to get different indexes'.format(MAX_RANDOM_TRIES))

            # Add the duplicate
            x_values[random_i_2] = x_values[random_i_1]

    relation_string = '{'  # type: str

    for i in range(len(x_values)):
        x = x_values[i]
        y = y_values[i]  # type: int

        pair = '({}, {})'.format(x, y)  # type: str
        if i < len(x_values) - 1:
            pair += ','
        relation_string += pair

    relation_string += '}'

    relation_formatted = '\({}\)'.format(relation_string)

    relation_widget = Widget(build_text_widget_options(relation_formatted))

    problem = [relation_widget]

    question_widgets = []

    def add_question_type(text):
        question_widgets.append(Widget(build_text_widget_options(questions[text])))

    if QUESTION_IS_FUNCTION in question_types:
        add_question_type(QUESTION_IS_FUNCTION)

    if (QUESTION_DOMAIN in question_types and QUESTION_RANGE in question_types) or QUESTION_DOMAIN_AND_RANGE in question_types:
        add_question_type(QUESTION_DOMAIN_AND_RANGE)
        if QUESTION_DOMAIN_AND_RANGE in question_types:
            question_types.remove(QUESTION_DOMAIN_AND_RANGE)
            question_types.extend([QUESTION_DOMAIN, QUESTION_RANGE])
    else:
        if QUESTION_DOMAIN in question_types:
            add_question_type(QUESTION_DOMAIN)
        if QUESTION_RANGE in question_types:
            add_question_type(QUESTION_RANGE)

    problem.extend(question_widgets)

    # solution

    def interval_from_continuous(values):
        min_n = math.inf
        max_n = -math.inf
        for i in values:
            if i < min_n:
                min_n = i
            if i > max_n:
                max_n = i
        return [min_n, max_n]

    def formatted_interval_from_continuous(values):
        interval = interval_from_continuous(values)
        interval_string = '[{}, {}]'.format(interval[0], interval[1])
        interval_formatted = fmath(interval_string)
        return interval_formatted

    def build_is_function_solution_text():
        response_modification_1 = 'Yes' if is_function else 'No'
        response_modification_2 = '' if is_function else 'not '
        response = '{}, this is {}a function.'.format(response_modification_1, response_modification_2)
        return Widget(build_text_widget_options(response))

    def build_domain_solution_text():
        formatted_interval = formatted_interval_from_continuous(x_values)
        response = 'The domain is {}.'.format(formatted_interval)
        return Widget(build_text_widget_options(response))

    def build_range_solution_text():
        formatted_interval = formatted_interval_from_continuous(y_values)
        response = 'The range is {}.'.format(formatted_interval)
        return Widget(build_text_widget_options(response))

    solution_types = {
        QUESTION_IS_FUNCTION: build_is_function_solution_text,
        QUESTION_DOMAIN: build_domain_solution_text,
        QUESTION_RANGE: build_range_solution_text,
    }

    solution_content = []

    for question_type in question_types:
        try:
            solution = solution_types[question_type]()
        except Exception:
            raise ValueError(
                'in relation_analysis: question type "{}" not found in solutions map'.format(question_type))

        solution_content.append(solution)

    # Wrap it in an array because that's what the client expects

    data = Problem(problem, solution_content)
    return data

@problem_type(
    description="Find if a given relation is a function",
    source="Created by Thomas Howe"
)
def is_relation_function():
    """
    :return:
    """
    return relation_analysis([QUESTION_IS_FUNCTION])

@problem_type(
    description="Find the domain and range of a given relation",
    source="Created by Thomas Howe"
)
def relation_domain_and_range():
    return relation_analysis([QUESTION_DOMAIN_AND_RANGE])

@problem_type(
    description="Find the domain of a given relation",
    source="Created by Thomas Howe"
)
def relation_domain():
    return relation_analysis([QUESTION_DOMAIN])

@problem_type(
    description="Find the range of a given relation",
    source="Created by Thomas Howe"
)
def relation_range():
    return relation_analysis([QUESTION_RANGE])