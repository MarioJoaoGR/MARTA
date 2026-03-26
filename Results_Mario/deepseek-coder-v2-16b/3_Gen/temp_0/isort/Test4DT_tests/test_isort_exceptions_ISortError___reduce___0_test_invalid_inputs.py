
import pytest

from isort.exceptions import ISortError


def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Attempt to call __reduce__ on a non-instance of ISortError
        non_instance = "not an instance"
        non_instance.__reduce__()
