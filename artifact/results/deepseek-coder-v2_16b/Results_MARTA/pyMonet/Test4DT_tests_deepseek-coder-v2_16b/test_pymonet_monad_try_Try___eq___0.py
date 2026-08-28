
import pytest
from pymonet.monad_try import Try

# Test valid input where Try is not a success and has a valid value
def test_valid_input():
    try1 = Try("error", False)  # Creates an instance where the operation failed due to "error".
    assert not try1.is_success
    assert try1.value == "error"

# Test edge case where Try is empty (is_success is True)
def test_edge_case():
    try2 = Try(None, True)  # Creates an instance where the operation was successful but value is None.
    assert try2.is_success
    assert try2.value is None

# Test invalid input to ensure it raises TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        Try()  # Attempting to create an instance without providing the required parameters should raise a TypeError.
