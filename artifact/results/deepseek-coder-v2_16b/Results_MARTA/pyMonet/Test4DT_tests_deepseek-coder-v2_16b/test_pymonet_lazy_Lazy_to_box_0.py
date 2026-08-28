
import pytest
from pymonet.lazy import Lazy

# Test valid input where Lazy is not None and has a valid function
def test_valid_input():
    lazy_object = Lazy(lambda: sum(range(10)))
    assert not lazy_object.is_evaluated
    result = lazy_object.get()  # Now the function will be called with range(10)
    assert lazy_object.is_evaluated
    assert result == sum(range(10))

# Test edge case where Lazy is None
def test_edge_case_none():
    lazy_object = Lazy(None)
    assert not lazy_object.is_evaluated
    with pytest.raises(TypeError):
        lazy_object.get()  # This should raise a TypeError since constructor_fn is None

# Test invalid input where no function is provided
def test_invalid_input():
    with pytest.raises(TypeError):
        Lazy()  # This should raise a TypeError as it requires a callable function
