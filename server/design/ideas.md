## Ideas

#### Problem types generate the variables, and then substitute them into existing JSON templates defined in seperate files with variable tokens like "$x", and "$variable\_name"

#### Ability to specify that the problem type is timed, and maybe how long it should take

#### A seperate "focus trainer" that just has me work on boring rote problems so I can train my focus

(#ideas)

## Problem types to add

### Quadratics

The quadratic generator will need a feature set specification. Whether it can have 0, 1, or 2 real roots, whether or not it needs to be easy to factor, what form (standard, vertex, factored, etc.), whether it conforms to some special rule, etc. It could get pretty complicated. Maybe test things out using Jupyter notebook?

Also, these problems should all be difficult. I want the most difficult problems. The answers shouldn't be fun and obvious.

IMPORTANT: Determine what parameters each function requires before writing a(ny) generator(s). This will make it more clear what kind of architecture to use.

#### When is y=n? (solve for n, n=f)

#### Completing the square

#### Finding vertex (\frac{-b}{2a}, f(\frac{-b}{2a}))

#### Determining number of roots

#### Determining y-intercept from different starting forms

#### Standard form from vertex and another point (could also provide a graph, but that might make things too easy--maybe there should be another problem type specifically with a graph)

#### Find minimum or maximum

#### List increasing and decreasing ranges

#### List transformations

#### Complete the square and realize that you now have vertex form 

This requires a generator that can give us a perfect square (x - h)^2 multiplied by some a a(x-h)^2 and then k a(x-h)^k. The best way to do this might not be to start from the vertex.

#### Find best fit for table of data (x-y pairs)

I could do this by:
- Generating a quadratic function (with very few restrictions, because the answer will be found via calculator anyway)
- Sampling it at several values of x
- Randomly adjusting the x and y values of the resulting pairs by a small amount (enough that the scatter diagram keeps its shape)
- Rounding pairs so they're easy to input into a calculator
- Computing a quadratic regression on pairs, then rounding the coefficients to two or three digits to keep it concise

It's important to note that the number of samples should be proportional to the maximum random distance. This way the shape of the function will be more obvious.

For the question: Put the pairs into a table widget and ask for a line of best fit. Remind that this requires a graphing calculator.

For the answer: Output the latex-formatted quadratic regression result.

WIDGET: Adjustment for graph that allows scatter-plot display. Client-side (w/ Plotly) configuration as it is will accept pair values, but it will display them as connected. This is as simple as adding a display type option in the graph widget options schema that allows for both connected and disconnected plots. The best way to do this would actually be per-graph instead of globally, since the graph widget will accept multiple expressions or tables.

#### Word problem types from Sullivan Algebra (4.4)

* Maximizing revenue
* Enclosing a rectangular field (without too much storytelling)
* Enclosing the most area with a field
* Analyzing the motion of a projectile
* Suspension bridge

#### Inequalities w/ quadratic functions (`x^2 - 4x - 12 <= 0, provide the domain in interval form`)

#### Factoring special forms

* Difference/sum of squares
* Difference/sum of cubes
* Et cetera


### Polynomials

#### Is f(x) = (either a polynomial or not a polynomial) a polynomial?

Trains rules about what is and isn't a polynomial.

#### How many turning points could this polynomial have at most?

To generate question, take the degree of the polynomial and subtract by one (n-1, where n is degree). Minimum degree should be 2, or first degree (linear) functions should be rare.

#### Give minimum degree by looking at turning points

Generate graph of polynomial with a known number of turning points (could be an interesting challenge to figure out how to generate a polynomial knowing how many visible turning points you want). Degree is at least n+1, where n is number of turning points.

#### Determine parity of multiplicity of root by looking at intercept on graph

#### Long division of polynomials with remainders

#### Given f(x), finding f(-x)

#### Finding zeros using long division (examples of this are in Sullivan 5.5, examples 5 and 6)

#### Find possible numbers of positive or negative roots by counting the variations in f(x) and f(-x)

#### List all potentional rational zeros of polynomial function with integer coefficients, using the Rational Zero theorem (5.5 problems 33-44)

#### Find real zeros of polynomial function using RZT, then factor using zeros (5.5 questions 45-56)

#### Find lower and upper bounds of polynomial function using synthetic division and the Bounds on Zeros theorem (5.5 questions 69-78)

In this question or any question using synthetic division, add a reminder in the answer box to include zero coefficients.

### Using bisection to approximate the real zero of a polynomial function (5.5, ex10 and problems 89-92)

Should use a calculator here. They say you can use the table feature on the graphing calculator, so you can set set column 2 to be the evaluation of column 1.

### Given the degree of a polynomial function and a set of real and complex zeros, find the rest (5.6 problems 7-16)

The way this works is simple.

1. For the degree d, pick a number between 3 and 6 
2. If the number is odd, pick a real zero
3. Set n to the largest even number within d, $n = floor(d/2)\*2$.
4. For every 

### Given real and complex zeros, find a polynomial function f. (5.6 problems 17-22)


### Find complex zeros of each polynomial function (5.6 problems 31-40)

Answer should be f in factored form.


### Functions

#### Find the domain of composite rational functions (6.1 problems 27-29)

The trick is to start at the innermost function and go outward.


### Rational functions

#### Determine whether rational function is even or odd

1/x is odd and 1/x^2 is even. To generate expressions for this problem, just apply transformations to rational expressions. The determining factor is the parity of the multiplicity.

Also, use any multiplicity for denominator factors. Just note whether it's odd or even.

#### Find asymptote of rational function, then determine if it intersects it

#### "Least cost of can" problems from Sullivan Algebra 5.3



### Uncategorized

#### Linear equations with unknown coefficients

This is poorly defined.

#### What is the domain of f + g? (where f and g (or any other functions with any letters) have domains that are closed, continuous intervals)

Problem should be split 75/25 between answers where f and g are a union, and answers where there is no union, and therefore no (real)? domain.

#### Solving triangles sides/angles with law of cosines

What would be nice is a widget that can render an arbitrary polygon and its angles, although it might be helpful to have a "blind" variant, where I have to come up with the answer based on the numbers alone.

Libraries:
* https://jsxgraph.uni-bayreuth.de/wp/about/index.html
* https://katex.org/

Two types:
* Getting a side length given both other side lengths and opposite angle
* Getting angle given all three side lengths

#### Solving triangle sides/angles with law of sines

(Flesh this out soon)

#### General word problems with variable names, subjects, and parameters

#### State domain, range of set/relation (just so I remember that they're like {1, 3, ... 5} instead of [1, 5])

#### Powers of fractions (like (5/2)^2)

#### Complex fractions

#### Reducing fractions

#### Fractions: invert and multiply; example: `(\frac{5}{\frac{2}{5}} = 5*\frac{5}{2}\)`

#### Practicing fraction division rules: [fraction\_rules](https://www.mathwords.com/f/fraction_rules.htm)

#### Inverting functions

* Invert this function, remembering that the end result needs to be explicitly f^{-1}(x) instead of f(y), so the problem solving process should start by swapping the x and the y
* Is this function g the inverse of function f? (true/false)
* Draw inverse relation

#### Various systems of equations problems

(Expand this into multiple types)

#### Inequalities with three parts

#### Converting between radians and degrees

#### Common radian angles

#### Evaluating powers of i (i^2, i^24, etc.)

#### Simplifying (important: not completely solving) linear equations with unknown coefficients (like ax+3x−b=5)

#### "Is this true?" questions, like "True or false: a(bc) = ab\*ac" (false)

#### Mental arithmetic speed runs (should set a baseline by doing this at a comfortable pace)

#### Identify shape classes from figures (multiple correct answers, like paralellogram and square)

#### Express radical as complex number (sqrt(-225))

#### Multiplying, dividing, adding, subtracting complex numbers (all seperate types)

#### Find equation of circle with center and radius

#### Find distance between two points

#### Subtraction w/ carrying (basic, ik)

(#questions)

## Finished problem types

#### Sum of consecutive integers "The sum of n consecutive integers is x. What is the jth number in this sequence?"
