
from pytutils.lazy.lazy_import import ScopeReplacer
import pytest

def test_invalid_input():
    # Test case for invalid input where scope is not a dictionary
    with pytest.raises(TypeError):
        ScopeReplacer("not_a_dict", lambda x, y, z: None, "name")
