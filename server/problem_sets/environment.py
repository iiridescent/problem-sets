from enum import Enum

class Environment(Enum):
    debug = 0
    prod = 1

    def is_debug(self):
        return self is Environment.debug