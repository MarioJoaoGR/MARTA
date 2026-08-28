
import pytest
from pymonet.monad_try import Try

# Test valid input where Try is successful and binds a function to it

# Test invalid input where Try is not successful and should return the original Try instance
def test_invalid_input():
    try_failure = Try("error", False)
    def double(x): return x * 2
    result = try_failure.bind(double)
    assert not result.is_success
    assert result.value == "error"