
import re

import pytest

from isort.sorting import _natural_keys


def test_error_handling():
    with pytest.raises(TypeError):
        # Test case for non-string input
        text = 12345
        _natural_keys(text)
