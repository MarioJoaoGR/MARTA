
import re

import pytest

from isort.sorting import _natural_keys


def test_edge_case_none():
    text = None
    with pytest.raises(TypeError):
        _natural_keys(text)
