# Electronic Structure Software Development: Best Practices and Tools

## Panel Discussion: Open-Source Development Best Practices & Tools

A brief presentation to kick off the discussion for the OSS dev best-practices
panel discussion at the Electronic Structure Software Development workshop
hosted by CECAM | October 10th, 2022

The presentation is in the form of a
[text-based Jupyter notebook using MyST markdown][myst-nb] and can be viewed
in presentation form via [RISE][RISE] or as a static website via
[sphinx][sphinx].

### Setup

To view the presentation locally you must install the dependencies.
Start by creating (if necessary) and entering a new environment:

```bash
python -m venv cecam-env
source cecam-env/bin/activate
```

Then install the requirements:

```bash
python -m pip install -r requirements.txt
```

### Viewing the presentation

In the `cecam-env` environment, launch Jupyter notebook client and open
`presentation.md`:

```bash
jupyter notebook presentation.md
```

In the notebook, you can enter/exit presentation mode with `alt+r`.
In presentation mode, use `<space>` to navigate to the next slide and
`<shift>+<space>` to move back.

[myst-nb]: https://myst-nb.readthedocs.io/en/latest/authoring/text-notebooks.html
[RISE]: https://rise.readthedocs.io/en/stable/
[sphinx]: https://www.sphinx-doc.org/en/master/
