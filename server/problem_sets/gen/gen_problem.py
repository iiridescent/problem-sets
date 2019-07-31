from dataclasses import dataclass
from typing import List, Union, Optional

from problem_sets.problem import Problem
from problem_sets.widget import Widget, TextWidgetOptions

GEN_FORMAT = "generated"


@dataclass()
class GenProblemContent:
    content: List[Widget]
    solution: List[Widget]
    debug_info: Optional[List[dict]] = None


class GenProblem(Problem):
    def __init__(self, set_id: str, id: int, content: List[Widget], solution: List[Widget],
                 debug_info: List[str] = None):
        """
        The output of a generated problem
        """

        super().__init__(set_id, id, GEN_FORMAT)
        if type(content) is not list or not all(isinstance(n, Widget) for n in content):
            raise ValueError(
                "parameter content in Problem must be of type List[Widget]"
            )

        if type(solution) is not list or not all(isinstance(n, Widget) for n in solution):
            raise ValueError(
                "parameter solution in Problem must be of type List[Widget]"
            )

        self.set_id = set_id
        self.id = id
        self.content = content
        self.solution = solution
        self.debug_info = debug_info

    def serialize(self):
        data = super(GenProblem, self).serialize().copy()

        serialized_problem_content_widgets = []
        for widget in self.content:
            problem_content_widget = widget
            serialized_problem_content_widgets.append(
                problem_content_widget.serialize()
            )

        serialized_solution_widgets = []
        for widget in self.solution:
            solution_widget = widget
            serialized_solution_widgets.append(solution_widget.serialize())

        data["content"] = serialized_problem_content_widgets

        data["solution"] = serialized_solution_widgets

        if self.debug_info:
            data["debug_info"] = str(self.debug_info)

        return data

    @classmethod
    def deserialize(cls, serialized: dict):
        pass

    @staticmethod
    def from_content(gen_problem_content: GenProblemContent, set_id: str, id: int):
        return GenProblem(set_id, id, gen_problem_content.content, gen_problem_content.solution,
                          gen_problem_content.debug_info)


def build_gen_problem_content(
        content: Union[List[Widget], List[str], str],
        solution: Union[List[Widget], List[str], str],
        debug_info: List[dict] = None,
):
    def process_strings_to_text_widgets(lines: Union[List[str], str]):
        lines = lines if isinstance(lines, List) else [lines]

        widgets = []
        for line in lines:
            widgets.append(Widget(TextWidgetOptions(line)))
        return widgets

    content_widgets = process_strings_to_text_widgets(content)
    solution_widgets = process_strings_to_text_widgets(solution)

    return GenProblemContent(content_widgets, solution_widgets, debug_info)
