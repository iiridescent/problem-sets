from sympy import symbols, Poly, Rational, latex
from numpy import random, around, arange
from numpy.random import randint
from problem_sets import create_full_text_problem, problem_type, render_testbed_problem, fmath

"""
5.5: The Real Zeros of a Polynomial Function
"""

@problem_type(
    description="Given a polynomial function $f(x)$, find $f(-x)",
    source="Sullivan Algebra 5.5"
)
def polynomial_function_find_negative():

    max_coeff_abs = 144
    min_degree = 2
    max_degree = 5

    degree = randint(min_degree, max_degree)

    coeffs = around(random.rand(6)*(max_coeff_abs*2))-max_coeff_abs

    x = symbols('x')

    # f(x)
    expr = 0
    # f(-x)
    neg_expr = 0

    # arange is half open; it doesn't include the top value, so we add 1
    for i in arange(degree-1)+1:
        coeff = Rational(coeffs[int(i)])
        power = Rational(degree-i)
        
        expr += coeff*(x)**power
        neg_expr += coeff*(-x)**power

    question = fmath("f(x) = "+latex(expr))

    answer = fmath("f(-x) = "+latex(neg_expr))

    return create_full_text_problem([question], [answer])