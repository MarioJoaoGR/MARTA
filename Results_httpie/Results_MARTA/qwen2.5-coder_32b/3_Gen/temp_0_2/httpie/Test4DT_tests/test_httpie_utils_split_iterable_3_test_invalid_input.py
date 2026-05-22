
import pytest
from httpie.utils import split_iterable

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test case where iterable is not an iterable type
        split_iterable(12345, lambda x: x % 2 == 0)
