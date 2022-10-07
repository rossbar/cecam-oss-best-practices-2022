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

+++ {"slideshow": {"slide_type": "slide"}}

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

+++ {"slideshow": {"slide_type": "slide"}}

# Software testing

+++ {"slideshow": {"slide_type": "fragment"}}

- **Unit tests** and **Integration testing** - both are important

+++ {"slideshow": {"slide_type": "fragment"}}

- Evaluating the health of your test suite
  * Coverage: necessary but not sufficient
  * Unit test crosstalk
    - Evaluate unit tests in random order (e.g. `pytest-randomly`)

+++ {"slideshow": {"slide_type": "fragment"}}

- Testing dependencies
  * Testing against development branch of major dependencies

% - Property-based testing (e.g. `hypothesis`)?

+++ {"slideshow": {"slide_type": "slide"}}

# Automated infrastructure

Continuous integration and continuous deployment (CI/CD) systems

+++ {"slideshow": {"slide_type": "fragment"}}

- Testing on different platforms, architectures, build-tool versions, etc.
  * Specifying jobs with testing matrix strategy

+++ {"slideshow": {"slide_type": "fragment"}}

- Triggering/scheduling jobs
  * On opening PR/push, scheduled jobs (`cron`), on-demand workflows

+++ {"slideshow": {"slide_type": "fragment"}}

- Inter-job & cross-workflow dependencies, concurrency
  * Conditional testing (i.e. only run full test suite if smoke tests pass)
  * Canceling currently-running jobs on new push

+++ {"slideshow": {"slide_type": "fragment"}}

- Clouds on the horizon: what happens when CI services are no longer free for OSS projects?
  * e.g. TravisCI
  * Self-hosted CI services?

+++ {"slideshow": {"slide_type": "slide"}}

# Adopting Software Best-Practices

Restating the point from the [workshop intro][workshop-intro]

> Allowing researchers with non-software backgrounds to employ best-practice
> methods when developing code

[workshop-intro]: https://www.cecam.org/workshop-details/1121

+++ {"slideshow": {"slide_type": "subslide"}}

**This is what the collaborative, review-based OSS development model is all about!**

+++ {"slideshow": {"slide_type": "fragment"}}

- Recognize the value each contributor brings with their unique skillset
  * Even more pronounced for domain-specific software dev

+++ {"slideshow": {"slide_type": "fragment"}}

- Don't let perfect be the enemy of good
  * The value of follow-up PRs & issues

+++ {"slideshow": {"slide_type": "fragment"}}

- Reviewer bandwidth is almost always a bottleneck
  * Ross' opinion as a reviewer: multiple, smaller PRs >>> one big one!

+++ {"slideshow": {"slide_type": "fragment"}}

- Being aware of the release cycle

+++ {"slideshow": {"slide_type": "slide"}}

# Documentation

Thinking about the different things a reader may be looking for.

+++ {"slideshow": {"slide_type": "subslide"}}

<center>

<img src="https://diataxis.fr/_images/diataxis.png" alt="Diataxis - a systematic framework for technical documentation authoring" width="1200">

[*Diátaxis framework:*][diataxis_home] *a systematic way of thinking about how
to organize documentation based on the various needs of users*

</center>

[diataxis_home]: https://diataxis.fr/

+++ {"slideshow": {"slide_type": "subslide"}}

- Reference guide auto-generated from source code (e.g. sphinx autodoc)

- Tutorials are **executable** and **regularly tested** to make sure they
  reflect changes in the underlying software.

- Example/thumbnail gallery (e.g. sphinx-gallery) is a nice format for how-tos
  * Especially when visualization is involved
