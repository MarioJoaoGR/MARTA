
import pytest
from itertools import count
from flutes.iterator import drop

def test_valid_input():
    # Test dropping 3 elements from a count iterator
    result = list(drop(3, count()))
    assert result == [3, 4, 5]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""