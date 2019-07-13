from fractions import Fraction
from numbers import Number
from numpy import round
from enum import Enum


def fmath(value, debug=False):
    value = (
        value.replace("%", "\%")
        .replace("$", "\$")
        # .replace("{", "\{")
        # .replace("}", "\}")
    )
    if debug == True:
        return f"${value}$"
    return f"\\({value}\\)"


def fcur(input):
    if int(input) == input:
        value = str(int(input))
    else:
        value = r"{:20,.2f}".format(input)

    return rf"${value.strip()}"


def iiw(input):
    if int(input) == input:
        return int(input)
    return input


def fper(input, decimal_points=3, mixed_fraction=False):
    value = iiw(round(input * 100, 3))

    if mixed_fraction:
        value = mfrac(value)

    return rf"{value}%"


def ord(num: float or int):
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


def mfrac(num):
    if int(num) == num:
        return str(int(num))

    whole = int(num)
    quotient = Fraction(num - whole).limit_denominator()
    return (
        f"{whole} \\small{{\\frac{{{quotient.numerator}}}{{{quotient.denominator}}}}}"
    )


def pluralize(singular: str, plural: str, num: Number):
    if num == 1:
        return singular

    return plural


class Axis(Enum):
    x = 0
    y = 1