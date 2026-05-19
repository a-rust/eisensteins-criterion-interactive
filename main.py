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

    return (mo,)


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


if __name__ == "__main__":
    app.run()
