
# Module: pymonet.lazy
# test_lazy.py
from pymonet.lazy import Lazy
import pytest

@pytest.fixture
def square():
    def square(x):
        return x * x
    return square

@pytest.fixture
def lazy_square():
    return Lazy(lambda x: x * x)

# Test initialization of Lazy instance with a function
def test_lazy_initialization(square):
    lazy = Lazy(square)
    assert callable(lazy.constructor_fn)
    assert not lazy.is_evaluated
    assert lazy.value is None

# Test forcing evaluation of the function stored in Lazy
def test_force_evaluation(lazy_square):
    result = lazy_square.get(5)
    assert isinstance(result, int)
    assert result == 25
    assert lazy_square.is_evaluated
    assert lazy_square.value == 25

# Test evaluating the function multiple times
def test_evaluation_multiple_times(lazy_square):
    first_eval = lazy_square.get(5)
    second_eval = lazy_square.get(5)
    assert first_eval == 25
    assert second_eval == 25
    assert lazy_square.is_evaluated
    assert lazy_square.value == 25

# Test evaluating with different arguments
def test_evaluation_with_different_args(lazy_square):
    result = lazy_square.get(3)
    assert isinstance(result, int)
    assert result == 9