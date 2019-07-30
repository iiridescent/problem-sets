#  Copyright (c) 2019 Thomas Howe

from problem_sets import Serializable


class StaticProblemSetEntity(Serializable):
    def __init__(self, id: str, source: str):
        self.id = id
        self.source = source

    def serialize(self) -> dict:
        # serialized_instruction_list = []
        #
        # for instruction in self.instruction:
        #     serialized_instruction_list.append(instruction.serialize())

        return {
            "id": self.id,
            # "instruction": serialized_instruction_list,
            "source": self.source
        }
