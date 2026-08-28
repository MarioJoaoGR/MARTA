
import pytest
from unittest.mock import patch, MagicMock
from pymonet.utils import memoize

# Test for memoize with a simple function
def test_memoize_simple():
    @memoize
    def add(x):
        return x + 10

    assert add(5) == 15
    assert add(5) == 15  # Should retrieve from cache

# Test for memoize with a function that takes multiple arguments and uses a custom key

# Test for memoize with a function that takes multiple arguments and uses a custom key

# Test for memoize with a function that takes multiple arguments and uses a custom key