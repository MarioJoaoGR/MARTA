
import pytest
from isort.sorting import naturally

def test_invalid_input():
    with pytest.raises(TypeError):
        naturally(123)  # Providing a non-iterable should raise TypeError
