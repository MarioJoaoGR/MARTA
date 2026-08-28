
import pytest
from pymonet.lazy import Lazy

# Example function to test the Lazy class
def square(x):
    return x * x

@pytest.fixture
def lazy_square():
    return Lazy(square)

def test_basic_initialization_and_evaluation(lazy_square):
    result = lazy_square.get(5)  # Evaluates the function with argument 5
    assert result == 25, f"Expected {25}, but got {result}"

def test_to_maybe_method(lazy_square):
    maybe_instance = lazy_square.to_maybe(5)