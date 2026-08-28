
import pytest
from pytutils.lazy.lazy_import import ScopeReplacer

# Test for valid input scenario

# Test for invalid input scenario
def test_invalid_input():
    with pytest.raises(Exception):
        replacer = ScopeReplacer('invalid', lambda: None, 'real_obj')