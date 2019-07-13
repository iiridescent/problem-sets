from dataclasses import dataclass
from typing import List

from numpy.random import rand, randint
from sympy import (Expr, Poly, Rational, UnevaluatedExpr, expand, latex, poly, solve, symbols)

from problem import Problem, create_full_text_problem
from problem_manager import problem_type
from util import fmath


@dataclass
class Quadratic:

    a: Rational
    b: Rational
    c: Rational

    def roots(self):
        return solve(self.as_expression())

    def vertex(self):
        x = symbols('x')

        vertex_x = -self.b/2*self.a
        vertex_yy = self.as_expression().subs(x, vertex_x)
        return (vertex_x, vertex_yy)

    def discriminant(self):
        return self.b**2-4*self.a*self.c

    def num_real_roots(self):
        discriminant = self.discriminant()
        if(discriminant > 0):
            return 2
        if(discriminant == 0):
            return 1
        if(discriminant < 0):
            return 0

    def as_expression(self):
        x = symbols('x')
        expression = Poly(Rational(self.a)*x**2 +
                          Rational(self.b)*x+Rational(self.c))
        return expression

    @staticmethod
    def from_point_vertex(point: (float, float), vertex: (float, float)):
        coefficients = point_vertex_to_standard(point, vertex).all_coeffs()

        return Quadratic(*coefficients)


def point_vertex_to_standard(point: (float, float), vertex: (float, float)) -> Poly:
    x = Rational(point[0])
    y = Rational(point[1])

    h = Rational(vertex[0])
    k = Rational(vertex[1])

    a = symbols('a')
    vertex_expr = (a*(x-h)**2)+k-y

    a = Rational(solve(vertex_expr)[0])

    x = symbols('x')

    vertex_expr = (a*(x-h)**2)+k

    return poly(vertex_expr)


# def standard_to_point_vertex(poly: Poly) -> Expr:


def generate_quadratic() -> Quadratic:
    # generate one of two roots
    # root =
    pass

@problem_type(
    description="Given a quadratic function in standard form, find vertex-intercept form"
)
def quadratic_function_find_vertex_intercept_form():
    
    # We may want to include fractions for more difficult problems in the future
    min_c = 1
    max_c = 6

    min_n = 1
    max_n = 30

    min_a = 1
    max_a = 5

    c = randint(min_c, max_c)
    n = randint(min_n, max_n)
    a = randint(min_a, max_a)

    c = -c if rand() < 0.5 else c

    x = symbols('x')

    expr = a*(x+c)**2

    # Expand into standard form

    expr = expand(expr)

    # Remove c^2

    expr = expr-a*c**2

    # Add n

    expr = expr+n

    eval_expr = a*(x+c)**2+n-(a*(c**2))

    problem_instruction = "Find vertex "

    problem_expr = fmath(latex(expr)+' = 0')

    problem_solution = fmath(latex(eval_expr)+' = 0')

    return create_full_text_problem([problem_expr], [problem_solution])
