
import pytest
from ansible.plugins.filter import mathstuff
from collections.abc import Hashable

# Assuming the function 'union' is defined in the 'mathstuff' module as per the provided code snippet
def union(environment, a, b):
    if isinstance(a, Hashable) and isinstance(b, Hashable):
        return list(set(a).union(set(b)))
    else:
        raise TypeError("Unsupported types")

# Test for valid inputs where both 'a' and 'b' are instances of Hashable (list or set)

# Test for invalid inputs where 'a' or 'b' is not an instance of Hashable (e.g., dict)
def test_invalid_types():
    environment = {}
    a = [1, 2, 3]
    b = {'key': 'value'}
    with pytest.raises(TypeError):
        union(environment, a, b)