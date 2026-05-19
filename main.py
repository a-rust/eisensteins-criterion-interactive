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
            [random.randint(-10, 10) for _ in range(2)]
        )
        polynomial_degree_value = random.randint(0, 3)
        prime_value = random.choice(primes_list)
    else:
        coefficient_bounds_value = sorted(
            [random.randint(-10, 10) for _ in range(2)]
        )
        polynomial_degree_value = random.randint(0, 3)
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
        start=0,
        stop=10,
        label="Degree",
        value=polynomial_degree_value,
        show_value=True,
    )

    primes = mo.ui.slider(
        steps=primes_list,
        label="p (Prime Number)",
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
    return (q,)


@app.cell
def _(mo, printing, q):
    # Display q(x)
    mo.vstack(
        align="center",
        # Convert q(x) to LaTeX expression
        items=[mo.md(rf"# $q(x) = {printing.latex(q)}$")],
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


if __name__ == "__main__":
    app.run()
