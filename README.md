# test-cython-scikit

A test project for a Python C extension module using Cython and the latest
(Jan 2025) packaging standards (scikit-build-core build backend).

## Usage
Install `uv` and `nox` in your environment (along with a recent python interpreter and C compiler of course) and run the following:

```shell
$ nox -l
Sessions defined in /Users/kzorba/WorkingArea/test-cython-scikit/noxfile.py:

* precommit -> Run the linter.
* pylint -> Run PyLint.
* tests -> Run the unit and regular tests.
- docs -> Build the docs. Pass --non-interactive to avoid serving. First positional argument is the target directory.
- build_api_docs -> Build (regenerate) API docs.
- build -> Build an SDist and wheel.

sessions marked with * are selected, sessions marked with - are skipped.

$ nox -s tests
nox > Running session tests
nox > Creating virtual environment (uv) using python in .nox/tests
nox > uv pip install '.[test]'
nox > pytest
================================================= test session starts ==================================================
platform darwin -- Python 3.12.5, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/kzorba/WorkingArea/test-cython-scikit
configfile: pyproject.toml
testpaths: tests
plugins: cov-6.0.0
collected 2 items

tests/test_compiled.py .                                                                                         [ 50%]
tests/test_package.py .                                                                                          [100%]

================================================== 2 passed in 0.14s ===================================================
nox > Session tests was successful.

$ nox -s build
...
(builds sdist and wheel in ./dist)
```

See also:

- https://learn.scientific-python.org/development/
- https://scikit-build-core.readthedocs.io
- https://github.com/astral-sh/uv
- https://nox.thea.codes/en/stable/
