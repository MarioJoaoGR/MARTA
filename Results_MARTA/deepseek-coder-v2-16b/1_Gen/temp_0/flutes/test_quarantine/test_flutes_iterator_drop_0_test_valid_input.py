
import pytest
from itertools import count
from flutes.iterator import drop

def test_valid_input():
    result = list(drop(5, count()))
    assert list(result) == [5, 6, 7, 8, 9]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""