from problem import Problem
from widget import Widget, TextWidgetOptions
from IPython.display import Markdown, Latex
from typing import List
from environment import Environment

class DebugProblemWrapper:
    def __init__(self, debug_info: [str], problem: Problem):
        self.debug_info = debug_info
        self.problem = problem


def render_testbed_problem(problem_fn):

    problem = problem_fn()

    debug_info = problem.debug_info

    body = ""

    if debug_info:
        body += "### debug info:\n\n"

        for line in debug_info:
            body += f"{line}\n\n"

    body += "### content:\n\n"

    body += widgets_to_string(problem.content)
    body += "\n\n### solution:\n\n"
    body += widgets_to_string(problem.solution)

    body = body.replace('\\(', '$').replace('\\)', '$')

    return Markdown(body)


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
