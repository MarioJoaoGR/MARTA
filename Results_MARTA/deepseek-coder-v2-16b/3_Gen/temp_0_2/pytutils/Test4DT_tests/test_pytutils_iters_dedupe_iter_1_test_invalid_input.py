
import pytest
from pytutils.iters import dedupe_iter

def test_invalid_input():
    with pytest.raises(TypeError):
        list(dedupe_iter(42))  # Passing a non-iterable object to check for TypeError
