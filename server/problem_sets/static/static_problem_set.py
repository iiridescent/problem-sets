from typing import List

from problem_sets import Serializable
from problem_sets.widget import Widget


class StaticProblemSet(Serializable):
    def __init__(self, id: str, instruction: List[Widget], source: str):
        self.id = id
        self.instruction = instruction
        self.source = source

    def serialize(self) -> dict:
        serialized_instruction_list = []

        for instruction in self.instruction:
            serialized_instruction_list.append(instruction.serialize())

        return {
            "id": self.id,
            "instruction": serialized_instruction_list,
            "source": self.source
        }
