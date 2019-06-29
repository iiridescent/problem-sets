from typing import List
from widget import Widget, TextWidgetOptions


class Problem:

    def __init__(self, content: List[Widget], solution: List[Widget], can_use_calculator=False):
        """

        :type content: List[any]
        :type solution: List[any]
        """

        # if type(content) is not List[Widget]:
        #     raise ValueError('parameter content in Problem must be of type List[Widget]')
        #
        # if type(solution) is not List[Widget]:
        #     raise ValueError('parameter solution in Problem must be of type List[Widget]')

        self.content = content
        self.solution = solution
        self.can_use_calculator = can_use_calculator

    def serialize(self):
        serialized_problem_content_widgets = []
        for widget in self.content:
            problem_content_widget = widget
            serialized_problem_content_widgets.append(problem_content_widget.serialize())

        serialized_solution_widgets = []
        for widget in self.solution:
            solution_widget = widget
            serialized_solution_widgets.append(solution_widget.serialize())

        return {
            'content': serialized_problem_content_widgets,
            'solution': serialized_solution_widgets
        }

def create_full_text_problem(content: List[str], solution: List[str], **pargs):
    def process_strings_to_text_widgets(strings: List[str]):
        widgets = []
        for string in strings:
            widgets.append(Widget(TextWidgetOptions(string)))
        return widgets

    content_widgets = process_strings_to_text_widgets(content)
    solution_widgets = process_strings_to_text_widgets(solution)

    return Problem(content_widgets, solution_widgets, **pargs)