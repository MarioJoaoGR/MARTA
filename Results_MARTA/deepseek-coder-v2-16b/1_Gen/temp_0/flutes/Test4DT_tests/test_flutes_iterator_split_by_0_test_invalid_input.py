
import pytest
from flutes.iterator import split_by

def test_invalid_input():
    # Test case where iterable is None
    with pytest.raises(TypeError):
        list(split_by(None, criterion=lambda x: bool(x)))
