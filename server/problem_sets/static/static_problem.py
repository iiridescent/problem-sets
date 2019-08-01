from typing import List, Union

from problem_sets.problem import Problem
from problem_sets.serialization import serialize_recursive
from problem_sets.static.data.static_content_entity import StaticContentEntity
from problem_sets.static.static_content import StaticContent, StaticContentType
from problem_sets.widget import Widget, ImageWidgetOptions, TextWidgetOptions

STATIC_FORMAT = "static"


class StaticProblem(Problem):

    def __init__(self, set_id: str, id: int, used: bool, content: Union[List[Widget], List[StaticContent]]):
        """
        API-facing information for a static problem
        """

        super().__init__(set_id, id, STATIC_FORMAT)

        # Convert any static content to widgets
        self.content = static_content_list_to_widget_list(content)
        self.used = used

    def serialize(self) -> dict:
        data = super(StaticProblem, self).serialize().copy()

        data['content'] = serialize_recursive(self.content)
        data['used'] = self.used

        return data


def static_content_to_widget(static_content: StaticContentEntity):
    if not isinstance(static_content, StaticContentEntity):
        return static_content
    if static_content.type == StaticContentType.image:
        return Widget(ImageWidgetOptions(str(static_content.id)))
    elif static_content.type == StaticContentType.text:
        return Widget(TextWidgetOptions(static_content.value))


def static_content_list_to_widget_list(static_content_list: List[StaticContent]):
    return list(static_content_to_widget(item) for item in static_content_list)
