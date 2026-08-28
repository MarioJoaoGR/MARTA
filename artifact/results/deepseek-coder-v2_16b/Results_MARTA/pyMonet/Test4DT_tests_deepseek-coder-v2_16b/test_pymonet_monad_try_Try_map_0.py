
import pytest
from pymonet.monad_try import Try

# Test valid input where Try is successful and can be mapped
def test_successful_map():
    try_success = Try("valid", True)
    mapped_try = try_success.map(lambda x: x + " mapped")
    assert isinstance(mapped_try, Try)
    assert mapped_try.is_success
    assert mapped_try.value == "valid mapped"

# Test invalid input where Try is successful but mapping function raises an error
def test_exception_in_mapper():
    try_success = Try("valid", True)
    with pytest.raises(IndexError):
        mapped_try = try_success.map(lambda x: x[10])  # This will raise a TypeError because "valid"[10] is out of bounds

# Test invalid input where Try is not successful and should return the original Try object
def test_failing_map():
    try_failure = Try("error", False)
    mapped_try = try_failure.map(lambda x: x + " mapped")
    assert isinstance(mapped_try, Try)
    assert not mapped_try.is_success
    assert mapped_try.value == "error"
