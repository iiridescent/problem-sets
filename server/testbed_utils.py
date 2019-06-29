from problem import Problem
from widget import Widget, TextWidgetOptions
from IPython.display import Markdown
from typing import List

def render_problem(problem: Problem):
    
    body = "### content:\n\n"
    
    body += widgets_to_string(problem.content)
    body += "\n\n### solution:\n\n"
    body += widgets_to_string(problem.solution)

    return Markdown(body)


def widgets_to_string(widgets):
    body = ""
    
    for widget in widgets:
        options = widget.options
        if type(options) == TextWidgetOptions:
            text = options.text
            body += text+"\n\n"
    # Get rid of the last newline at the end
    return body[:-2]