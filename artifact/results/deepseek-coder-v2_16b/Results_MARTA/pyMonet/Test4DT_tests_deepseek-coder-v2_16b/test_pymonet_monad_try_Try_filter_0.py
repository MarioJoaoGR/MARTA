
import pytest
from pymonet.monad_try import Try

# Test valid input scenario
def test_valid_input():
    try1 = Try(42, True)
    assert try1.value == 42
    assert try1.is_success is True

# Test edge case scenario with None value and False is_success
def test_edge_case():
    try_none = Try(None, False)
    assert try_none.value is None
    assert try_none.is_success is False

# Test invalid input handling for filter method
def test_invalid_input():
    try_fail = Try('error', False)
    filtered_try = try_fail.filter(lambda x: isinstance(x, int))
    assert filtered_try.value == 'error'
    assert filtered_try.is_success is False
