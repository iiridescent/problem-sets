#  Copyright (c) 2019 Thomas Howe

from types import FunctionType

from IPython import get_ipython
from IPython.display import display, Markdown, Latex

from problem_sets.problem import Problem
from problem_sets.widget import TextWidgetOptions


class DebugProblemWrapper:
    def __init__(self, debug_info: [str], problem: Problem):
        self.debug_info = debug_info
        self.problem = problem


def render_testbed_problem(problem_fn, random_seed=None):

    problem = problem_fn(random_seed)
    debug_info = problem.debug_info
    random_seed = problem.id

    body = ""

    if debug_info or random_seed:
        body += "### debug info:\n\n"

        if random_seed:
            body += f"random seed: {random_seed}\n\n"

        for line in debug_info:
            body += f"{line}\n\n"

    body += "### content:\n\n"

    body += widgets_to_string(problem.content)
    body += "\n\n### solution:\n\n"
    body += widgets_to_string(problem.solution)

    body = body.replace("\\(", "$").replace("\\)", "$")

    display(Markdown(body))


def render_latex(content: str):
    return Latex(str)


def widgets_to_string(widgets):
    body = ""

    for widget in widgets:
        options = widget.options
        if type(options) == TextWidgetOptions:
            text = options.text
            body += text + "\n\n"
    # Get rid of the last newline at the end
    return body[:-2]


def debug(random_seed=None):
    """
    Decorator: given a problem generator function 'fun', render its output.
    """
    def inner(fun: FunctionType):
        if get_ipython() is not None:
            render_testbed_problem(fun, random_seed)
            
        return fun

    return inner
