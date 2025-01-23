from __future__ import annotations

import importlib.metadata

import test_cython_scikit as m


def test_version():
    assert importlib.metadata.version("test_cython_scikit") == m.__version__
