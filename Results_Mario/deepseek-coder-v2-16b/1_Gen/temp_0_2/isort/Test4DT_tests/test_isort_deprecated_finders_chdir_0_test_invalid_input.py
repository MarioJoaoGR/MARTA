
import os
from collections.abc import Iterator
import pytest
from isort.deprecated.finders import chdir

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test that passing an invalid type (e.g., a list) to chdir raises a TypeError
        with chdir([1, 2, 3]):
            pass
