
import pytest
from isort.sorting import _atoi  # Assuming this is the correct module and function name

def test_invalid_input():
    assert _atoi("abc") == "abc"
