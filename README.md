# Polynomial Irreducibility via Eisenstein's Criterion

This is an interactive [marimo](https://github.com/marimo-team/marimo) notebook that applies [Eisenstein's criterion](https://en.wikipedia.org/wiki/Eisenstein's_criterion) to test a randomly generated polynomial $q(x)\in \mathbb{Z}[x]$ for [irreducibility](https://en.wikipedia.org/wiki/Irreducible_polynomial) over $\mathbb{Q}$

# Eisenstein's Criterion Overview

Let

$$q(x) = a_0 + a_1(x) + a_2(x^2) + ... + a_n(x^n), a_i \in \mathbb{Z}$$

Eisenstein's criterion states that $q(x)$ is irreducible over $\mathbb{Q}$ if there exists a prime number $p\in \mathbb{Z}$ such that all three conditions are met:
* $p$ divides each $a_i$ for $0 \leq i < n$
* $p$ does not divide $a_n$
* $p^2$ does not divide $a_0$

---
![Example 1](/examples/test-success.png)

---
![Example 2](/examples/test-fail.png)