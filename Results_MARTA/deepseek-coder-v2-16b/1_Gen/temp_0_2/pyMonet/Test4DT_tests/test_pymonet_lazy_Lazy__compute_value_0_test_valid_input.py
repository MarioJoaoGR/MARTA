
import pytest
from pymonet.lazy import Lazy

# Define the square function for testing
def square(x):
    return x * x

@pytest.fixture
def lazy_instance():
    return Lazy(square)

def test_valid_input(lazy_instance):
    # Initial state should be not evaluated and value should be None
    assert not lazy_instance.is_evaluated
    assert lazy_instance.value is None
    
    # Call fold to evaluate the function
    result = lazy_instance._compute_value(5)
    
    # After evaluation, it should be marked as evaluated and have a value
    assert lazy_instance.is_evaluated
    assert lazy_instance.value == 25
    assert result == 25
