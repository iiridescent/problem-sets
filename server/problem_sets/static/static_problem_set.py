from dataclasses import dataclass

from problem_sets.serialization import serialize_recursive
from problem_sets.static.data.static_problem_set_entity import StaticProblemSetEntity
from problem_sets.static.static_problem import static_content_list_to_widget_list


@dataclass
class StaticProblemSet(StaticProblemSetEntity):

    def serialize(self) -> dict:
        data = self.__dict__.copy()
        del data['instruction_contents']
        del data['answer_contents']

        data['instructionContents'] = serialize_recursive(
            static_content_list_to_widget_list(self.instruction_contents))
        data['answerContents'] = serialize_recursive(static_content_list_to_widget_list(self.answer_contents))
        return data

    @classmethod
    def deserialize(cls, serialized: dict):
        pass
