from fractions import Fraction
from numbers import Number
from numpy import around
from numpy.random import randint, choice
from enum import Enum
from problem_sets.environment import Environment
from typing import Union, Tuple, List
from sympy import root as sp_root, latex as sp_latex
from problem_sets.math import ord

def fmath(value):
    """
    Format MATH
    Add latex surrounding brackets ('\\(' and '\\)') and escape special characters ('$' --> '\\$')
    """
    if isinstance(value, Number):
        value = str(value)
    value = value.replace("%", "\\%").replace("$", "\\$")
    return f"\\({value}\\)"


def fcur(input):
    """
    Format CURrency
    """
    if int(input) == input:
        value = str(int(input))
    else:
        value = r"{:20,.2f}".format(input)

    return rf"${value.strip()}"


def iiw(input, precision=5):
    """
    convert to Int If Whole
    Convert number to an int if it is whole (rounded to 5 decimal points by default)
    """

    rounded = around(input, precision)

    if not isinstance(input, int) and int(rounded) == rounded:
        return int(rounded)
    return input


def fper(input, precision=3, mixed_fraction=False):
    """
    Format PERcentage
    Multiply input by 100 and round it to the number of decimal points specified by precision (default 3)
    """
    value = iiw(around(input * 100, precision))

    if mixed_fraction:
        value = ffrac(value)

    return rf"{value}%"


def ford(num: Number):
    return f"{num}{ord(num)}"


def ffrac(num: Union[Number, Tuple[Number, Number]], mixed=True):
    """
    Format FRACtion
    Convert 'num' (which can be either a number or a tuple with two elements, 
    one for numerator and one for denominator) into latex-formatted fraction
    """
    if isinstance(num, tuple):
        if isinstance(num[0], Number) and isinstance(num[1], Number):
            num = num[0] / num[1]
        else:
            raise TypeError("'num' must be number or tuple of numbers")

    if int(num) == num:
        return str(int(num))

    whole = int(num) if mixed else 0
    quotient = Fraction(num - whole).limit_denominator()

    sign = "-" if quotient < 0 else ""

    output = f"\\small{{{sign}\\frac{{{abs(quotient.numerator)}}}{{{abs(quotient.denominator)}}}}}"

    if whole != 0:
        output = f"{whole} " + output

    return output


#%%
def froot(root: Number, degree: Number = 2, simplify=True):
    """
    Format ROOT
    Convert 'root' to formatted Latex math root by representing it
    as an nth degree root of root^n
    """

    root = iiw(root)

    if isinstance(root, int):
        return str(root)

    square = iiw(root ** degree)
    print(square)
    sqrt = sp_root(square, degree) if simplify else f"\\sqrt{{{square}}}"
    return sp_latex(sqrt)


def fexpprod(prod: Number, degree: Number = 2, simplify=True):
    """
    Format EXPonential PRODuct
    Get the 'degree' nth root of prod (prod^(1/n)) and output it as formatted Latex
    """

    return froot(prod ** (1 / degree), degree, simplify)


def fplural(singular: str, plural: str, num: Number):
    """
    Format PLURAL
    Given the singular and plural form of a word, return the plural form if num != 1
    """
    if num == 1:
        return singular

    return plural


def fsign(n, imply_pos=True):
    """
    Format SIGN prefix
    '-' if n < 0 else '' (or '+' if imply_pos is false)
    """
    return "-" if n < 0 else "" if imply_pos else "+"


class LatexBracket(Enum):
    round = ("(", ")")
    square = ("[", "]")
    curly = ("\\{", "\\}")


def fbra(
    value: Union[str, Number],
    bracket: LatexBracket = LatexBracket.round,
    tall=False,
):
    """
    Format BRAcket
    Wrap expression in parentheses
    """

    value = str(value)
    brackets = bracket.value
    opening = brackets[0]
    closing = brackets[1]

    if tall:
        opening = f"\\left{opening}"
        closing = f"\\right{closing}"

    return f"{opening}{value}{closing}"


class LatexTrigFunction(Enum):
    sin = "sin"
    cos = "cos"
    tan = "tan"
    csc = "csc"
    sec = "sec"
    cot = "cot"
    arcsin = "sin^{-1}"
    arccos = "cos^{-1}"
    arctan = "tan^{-1}"
    arccsc = "csc^{-1}"
    arcsec = "sec^{-1}"
    arccot = "cot^{-1}"


def ftrigfun(value: Union[str, Number], function: LatexTrigFunction):
    """
    Format trig function with value
    """

    formatted_value = f"{{{str(value)}}}"

    return f"\\{function.value}{formatted_value}"
