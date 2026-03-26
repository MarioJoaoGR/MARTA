
import pytest
from pymonet.lazy import Lazy

def square(x):
    return x * x

@pytest.fixture
def lazy():
    return Lazy(square)

def test_valid_input(lazy):
    result = lazy.get(5)
    assert result == 25
    assert lazy.is_evaluated is True
