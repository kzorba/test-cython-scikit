from __future__ import annotations

import test_cython_scikit as m


def test_square():
    assert m.square(3) == 9
