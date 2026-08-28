
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    try1 = Try(42, True)
    result1 = try1.filter(lambda x: isinstance(x, int))
    assert result1.is_success is True
    assert result1.value == 42


def test_filter_with_invalid_value():
    try5 = Try(None, True)
    result2 = try5.filter(lambda x: x is not None)
    assert result2.is_success is False