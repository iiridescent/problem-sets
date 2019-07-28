from typing import List
from numpy.random import randint

def pick_from_list(list: List, elements = 1):
    """
    pick n elements from list
    """

    # We're going to remove items from this list, so we
    # want the value instead of the reference

    list = list.copy()

    if not isinstance(elements, int):
        raise TypeError(f"'elements' must be type int, not {type(elements)}")

    if elements < 1:
        raise ValueError("'elements' must be an integer >= 1")

    if elements > len(list):
        raise ValueError("'elements' must be <= length of 'list'")

    output = []

    for _ in range(elements):
        index = randint(0, len(list))
        element = list[index]
        
        output.append(element)

        del list[index]


    # If output is only one item, return just that item
    if len(output) == 1:
        return output[0]
    
    return output