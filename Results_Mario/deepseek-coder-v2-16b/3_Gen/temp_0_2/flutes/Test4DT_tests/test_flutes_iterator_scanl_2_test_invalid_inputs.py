
import pytest
from flutes.iterator import scanl

# Define a simple binary function for testing
def add(x: int, y: int) -> int:
    return x + y

# Test cases for invalid inputs
@pytest.mark.parametrize("func, iterable, initial", [
    (None, [1, 2, 3], 0),          # func is None
    (add, None, 0),                # iterable is None
    (add, [1, 2, 3], None)        # initial is None
])
def test_invalid_inputs(func, iterable, initial):
    with pytest.raises(TypeError):
        list(scanl(func, iterable, initial))
