# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.6",
#     "sympy==1.14.0",
# ]
# ///

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import math, random
    from sympy import primerange, symbols, Poly, printing
    from sympy.core.random import _randint

    return Poly, mo, primerange, printing, random, symbols


@app.cell
def _(mo):
    # Overview of Project
    mo.vstack(
        align="center",
        gap=2,
        items=[
            mo.md("# Polynomial Irreducibility via Eisenstein's Criterion"),
            mo.md(
                r"### This is an interactive notebook that illustrates [Eisenstein's criterion](https://en.wikipedia.org/wiki/Eisenstein's_criterion)"
            ),
            mo.md("## Overview of Theorem"),
            mo.md(
                r"### Let $q(x) = a_0 + a_1(x) + a_2(x^2) + ... + a_n(x^n)$, $a_i \in \mathbb{Z}$"
            ),
            mo.md(
                r"### $q(x)$ is irreducible over $\mathbb{Q}$ if there exists a prime number $p\in \mathbb{Z}$ such that all three conditions are met:"
            ),
            mo.md("### $p$ divides each $a_i$ for $0 \leq i < n$"),
            mo.md("### $p$ does not divide $a_n$"),
            mo.md("### $p^2$ does not divide $a_0$"),
        ],
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _(mo):
    mo.vstack(align="center", items=[mo.md("# Demo")])
    return


@app.cell
def _(mo):
    # Button to randomize user input values
    randomize_button = mo.ui.run_button(label="Randomize")
    return (randomize_button,)


@app.cell
def _(primerange, random, randomize_button):
    # Parameters for randomly generated polynomial q(x) (coefficient bounds and degree)

    # Range of prime numbers to check q(x) for irreducibility via Eisenstein's Criterion
    primes_list = list(primerange(1, 101))

    if randomize_button.value:
        coefficient_bounds_value = sorted(
            [random.randint(-100, 100) for _ in range(2)]
        )
        polynomial_degree_value = random.randint(1, 3)
        prime_value = random.choice(primes_list)
    else:
        coefficient_bounds_value = sorted(
            [random.randint(-100, 100) for _ in range(2)]
        )
        polynomial_degree_value = random.randint(1, 3)
        prime_value = random.choice(primes_list)
    return (
        coefficient_bounds_value,
        polynomial_degree_value,
        prime_value,
        primes_list,
    )


@app.cell
def _(
    coefficient_bounds_value,
    mo,
    polynomial_degree_value,
    prime_value,
    primes_list,
):
    # User inputs (to update the parameters of q(x))
    coefficient_bounds = mo.ui.range_slider(
        start=-100,
        stop=100,
        value=coefficient_bounds_value,
        label="Coefficient Bounds",
        show_value=True,
    )

    polynomial_degree = mo.ui.slider(
        # Not counting degree 0 polynomials
        start=1,
        stop=10,
        label="Degree",
        value=polynomial_degree_value,
        show_value=True,
    )

    primes = mo.ui.slider(
        steps=primes_list,
        label="p",
        value=prime_value,
        show_value=True,
    )
    return coefficient_bounds, polynomial_degree, primes


@app.cell
def _(Poly, coefficient_bounds, polynomial_degree, symbols):
    # Construct q(x)
    ri = _randint()
    coefficients = [
        # Coefficients are bounded by the coefficient_bounds slider
        ri(coefficient_bounds.value[0], coefficient_bounds.value[1])
        # Number of coefficients is determined by the degree of q(x)
        for _ in range(polynomial_degree.value + 1)
    ]

    # Define q(x)
    q = Poly(coefficients, symbols("x")).as_expr()
    return coefficients, q


@app.cell
def _(irreducible_polynomial, mo, printing, q):
    # Display q(x)
    mo.vstack(
        align="center",
        # Convert q(x) to LaTeX expression
        items=[
            mo.md(
                rf"# <span style='color: green;'>$q(x) = {printing.latex(q)}$ </span>"
            )
            if irreducible_polynomial
            else mo.md(
                rf"# <span style='color: red;'>$q(x) = {printing.latex(q)}$ </span>"
            )
        ],
    )
    return


@app.cell
def _(coefficient_bounds, mo, polynomial_degree, primes, randomize_button):
    user_inputs = mo.vstack(
        align="center",
        gap=1,
        items=[randomize_button, coefficient_bounds, polynomial_degree, primes],
    )
    return (user_inputs,)


@app.cell
def _(user_inputs):
    user_inputs
    return


@app.cell
def _(mo):
    mo.vstack(align="center", items=[mo.md("# Conditions")])
    return


@app.cell
def _(coefficients, mo, primes):
    # Condition one: $p$ divides each $a_i$ for $0 \leq i < n$

    # Counter to keep track of how many coefficients $p$ divides
    divisible_counter = 0

    # List for displaying whether or not $p$ divides $a_i$ for $0 \leq i < n$
    divisible_list = []

    # Checks coefficients $a_i$ for $0 \leq i < n$
    for item in coefficients[1:]:
        if item % primes.value == 0:
            divisible_list.append(
                mo.md(
                    rf"## <span style='color: green;'>${primes.value} \mid {item}$ </span>"
                )
            )
            divisible_counter += 1
        else:
            divisible_list.append(
                mo.md(
                    rf"## <span style='color: red;'>${primes.value} \nmid {item}$ </span>"
                )
            )

    # Since checking coefficients $a_i$ for $0 \leq i < n$, condition one is met if divisible_counter is equal to the number of coefficients - 1
    condition_one_met = divisible_counter == len(coefficients) - 1

    condition_one_result = mo.vstack(
        align="center",
        items=[
            mo.md(
                r"## <span style='color: green;'>$p$ divides each $a_i$ for $0 \leq i < n$ </span>"
            )
            if condition_one_met
            else mo.md(
                r"## <span style='color: red;'>$p$ divides each $a_i$ for $0 \leq i < n$ </span>"
            ),
            mo.vstack(divisible_list),
        ],
    )
    return condition_one_met, condition_one_result


@app.cell
def _(coefficients, mo, primes):
    # Condition two: $p$ does not divide $a_n$
    condition_two_met = coefficients[0] % primes.value != 0

    condition_two_result = mo.vstack(
        align="center",
        items=[
            mo.md(
                "## <span style='color: green;'>$p$ does not divide $a_n$ </span>"
            )
            if condition_two_met
            else mo.md(
                "## <span style='color: red;'>$p$ does not divide $a_n$ </span>"
            ),
            mo.md(
                rf"## <span style='color: green;'>${primes.value} \nmid {coefficients[0]}$ </span>"
            )
            if condition_two_met
            else mo.md(
                rf"## <span style='color: red;'>${primes.value} \mid {coefficients[0]}$ </span>"
            ),
        ],
    )
    return condition_two_met, condition_two_result


@app.cell
def _(coefficients, mo, primes):
    # Condition three: $p^2$ does not divide $a_0$
    condition_three_met = coefficients[-1] % pow(base=primes.value, exp=2) != 0

    condition_three_result = mo.vstack(
        align="center",
        items=[
            mo.md(
                "## <span style='color: green;'>$p^2$ does not divide $a_0$ </span>"
            )
            if condition_three_met
            else mo.md(
                "## <span style='color: red;'>$p^2$ does not divide $a_0$ </span>"
            ),
            mo.md(
                rf"## <span style='color: green;'>${pow(base=primes.value, exp=2)} \nmid {coefficients[-1]}$ </span>"
            )
            if condition_three_met
            else mo.md(
                rf"## <span style='color: red;'>${pow(base=primes.value, exp=2)} \mid {coefficients[-1]}$ </span>"
            ),
        ],
    )
    return condition_three_met, condition_three_result


@app.cell
def _(condition_one_result, condition_three_result, condition_two_result, mo):
    mo.hstack(
        justify="space-between",
        items=[condition_one_result, condition_two_result, condition_three_result],
    )
    return


@app.cell
def _(condition_one_met, condition_three_met, condition_two_met):
    # Result
    irreducible_polynomial = (
        condition_one_met and condition_two_met and condition_three_met
    )
    return (irreducible_polynomial,)


if __name__ == "__main__":
    app.run()
