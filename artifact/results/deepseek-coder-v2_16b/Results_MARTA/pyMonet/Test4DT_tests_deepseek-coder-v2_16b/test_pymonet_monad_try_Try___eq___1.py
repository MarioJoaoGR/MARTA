
import pytest
from pymonet.monad_try import Try

# Test valid input where Try is not a success and has a valid value
def test_valid_input():
    try1 = Try("error", False)  # Creates an instance where the operation failed due to "error".
    assert not try1.is_success
    assert try1.value == "error"

# Test edge case where Try is a success (is_success is True)
def test_edge_case():
    try2 = Try(42, True)  # Creates an instance where value is 42 and operation was successful.
    assert try2.is_success
    assert try2.value == 42

# Test invalid inputs to ensure it raises TypeError
def test_invalid_inputs():
    with pytest.raises(TypeError):
        Try()
