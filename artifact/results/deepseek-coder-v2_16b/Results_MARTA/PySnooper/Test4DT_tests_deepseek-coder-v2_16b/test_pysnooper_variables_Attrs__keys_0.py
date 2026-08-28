
import pytest
from pysnooper.variables import Attrs
import itertools

# Test valid input scenario

# Test none input scenario
def test_none_input():
    with pytest.raises(TypeError):
        keys_iterator = Attrs._keys(None)