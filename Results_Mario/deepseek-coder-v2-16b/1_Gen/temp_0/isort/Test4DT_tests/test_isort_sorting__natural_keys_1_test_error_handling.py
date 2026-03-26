
import re
from isort.sorting import _natural_keys
import pytest

def test_error_handling():
    with pytest.raises(TypeError):
        # Test case for non-string input
        text = 12345
        _natural_keys(text)
