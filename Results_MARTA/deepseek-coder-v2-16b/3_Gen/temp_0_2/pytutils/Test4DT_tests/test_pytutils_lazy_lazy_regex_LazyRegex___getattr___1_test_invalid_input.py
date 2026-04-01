
import pytest
import re
from pytutils.lazy.lazy_regex import LazyRegex

def test_invalid_input():
    with pytest.raises(TypeError):
        lazy_regex = LazyRegex()
        # Accessing an invalid attribute should raise a TypeError, which is subclass of Exception and thus covers the requirement.
        getattr(lazy_regex, 'invalid_attribute')
