
import pytest

from isort.exceptions import ISortError


def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Passing an invalid argument to trigger TypeError
        ISortError(some_invalid_argument="invalid")
