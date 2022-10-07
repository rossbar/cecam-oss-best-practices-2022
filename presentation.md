---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"slideshow": {"slide_type": "slide"}}

# Panel Discussion: Tools and Best-Practices for Open-Source Scientific Software

<center>

#### Electronic Structure Software Development Workshop | October 10th, 2022

</center>

 - [Ross Barnowski](https://bids.berkeley.edu/people/ross-barnowski) `rossbar@berkeley.edu` | [@rossbar](https://github.com/rossbar) on GitHub

 - **TODO: Insert Rohit info here**

[Centre Européen de Calcul Atomique et Moléculaire][cecam]

[cecam]: https://www.cecam.org/

+++ {"slideshow": {"slide_type": "slide"}}

# Quick introductions

+++ {"slideshow": {"slide_type": "subslide"}}

### I'm Ross ([@rossbar](https://github.com/rossbar))

+++ {"slideshow": {"slide_type": "fragment"}}

- Scientific software developer at the [Berkeley Institute for Data Science][BIDS]
  * My background is in radiation instrumentation

% PETSc joke?

[BIDS]: https://bids.berkeley.edu/people/ross-barnowski

+++ {"slideshow": {"slide_type": "fragment"}}

- I am a member of the [Scientific Python][scientific-python] community,
  supporting the libraries of scientific Python ecosystem.
  * Active contributor to [NumPy][numpy] and [NetworkX][networkx]
  * Work to support cross-project [coordination][specs] and
    [communication][discuss]

[scientific-python]: https://scientific-python.org/
[numpy]: https://numpy.org
[networkx]: https://networkx.org
[specs]: https://scientific-python.org/specs/
[discuss]: https://discuss.scientific-python.org/

+++ {"slideshow": {"slide_type": "subslide"}}

### TODO: Rohit intro!

+++ {"slideshow": {"slide_type": "subslide"}}

# Framing the discussion

+++ {"slideshow": {"slide_type": "fragment"}}

> - Ensuring that the library and codes are sufficiently **tested** and correct by
>   providing tests that check functionality and correctness.
> - **Automating infrastructure** for testing, building and addressing compiler
>   compatibility issues.
> - Allowing **researchers with non-software backgrounds to employ best-practice
>   methods when developing code**, such as for performance critical aspects as
>   well as for maintainability and interface issues.
> - Providing sufficient **documentation**, both for developers interfacing
>   libraries in a hosting code, and for users who require knowledge of the
>   functionality provided.
