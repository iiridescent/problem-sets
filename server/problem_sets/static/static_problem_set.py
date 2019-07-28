class StaticProblemSet:
    def __init__(self, id: str, instruction: str, source: str):
        self.id = id
        self.instruction = instruction
        self.source = source

    def serialize(self):
        return {
            "id": self.id,
            "instruction": self.instruction,
            "source": self.source
        }
