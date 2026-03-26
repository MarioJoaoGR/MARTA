
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_invalid_inputs():
    with pytest.raises(TypeError):
        LazyRegex().__setstate__(123)  # Passing an invalid input type to trigger TypeError
