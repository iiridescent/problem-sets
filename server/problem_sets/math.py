#%%
from fractions import Fraction
from numbers import Number
from numpy import around
from numpy.random import randint, choice
from enum import Enum
from problem_sets.environment import Environment
from typing import Union, Tuple, List
from sympy import root as sp_root, latex as sp_latex

#%%


def ord(num: Number):
    """
    find ORDinal suffix for number
    0 --> '0th'
    1 --> '1st'
    47 --> '47th'
    562 --> '562nd'
    """
    # These should probably be constants
    th = "th"
    st = "st"
    rd = "rd"
    nd = "nd"

    string_value = str(num)

    digits_string = string_value[-2:]

    # 11th, 12th, 13th (there may be a more optimized pattern here)
    if digits_string == "11" or digits_string == "12" or digits_string == "13":
        return th

    digits_string = digits_string[-1:]

    digits = float(digits_string) if type(num) is float else int(digits_string)

    ordinal_indicator_map = {
        0: th,
        1: st,
        2: nd,
        3: rd,
        4: th,
        5: th,
        6: th,
        7: th,
        8: th,
        9: th,
    }

    return ordinal_indicator_map[digits]


class Axis(Enum):
    x = 0
    y = 1


def move_point_along_axis(p: (Number, Number), m: Number, axis: Axis):
    if not p or not m or not axis:
        raise ValueError()

    if axis == Axis.y:
        p[1] += m
    elif axis == Axis.x:
        p[0] += m

    return p


#%%
def randint_gap(low, high, gap_low, gap_high):
    """
    Random integer on interval excluding gap
    Return integer either on interval from low to gap_low inclusive [low, gap_low]
    or on interval from gap_high to high inclusive [gap_high, high]
    """

    if low > high or gap_low > gap_high:
        raise ValueError('randint_gap expects low, high, gap_low, gap_high where low < high, gap_low < gap_high')

    if gap_low <= low or gap_high >= high:
        raise ValueError('randint_gap expects gap_low > low, gap_high < high')
    
    return int(choice([randint(low, gap_low+1), randint(gap_high, high+1)]))


def randint_gap_tuple(range: Tuple[Number, Number], gap: Tuple[Number, Number]):
    """
    Same thing as randint_gap, but with tuples as arguments
    """
    return randint_gap(range[0], range[1], gap[0], gap[1])
#%%

def sign(n):
    """
    Get sign multiplicand: 1 if n >= 0, -1 if n < 0
    """
    return 1 if n >= 0 else -1