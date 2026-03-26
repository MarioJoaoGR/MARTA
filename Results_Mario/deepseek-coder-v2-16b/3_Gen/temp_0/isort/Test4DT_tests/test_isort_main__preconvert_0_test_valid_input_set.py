
from enum import Enum
from pathlib import Path

import pytest

from isort.main import _preconvert


def test_valid_input_set():
    # Test case where item is a set
    test_set = set([1, 2, 3])
    result = _preconvert(test_set)
    assert result == [1, 2, 3]
