
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_invalid_input():
    with pytest.raises(TypeError):
        LazyRegex().__setstate__(None)  # Passing None should raise a TypeError
