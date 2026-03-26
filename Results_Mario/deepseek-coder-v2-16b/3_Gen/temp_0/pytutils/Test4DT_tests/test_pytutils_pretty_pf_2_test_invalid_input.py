
import pytest
from unittest.mock import patch
from pytutils.pretty import pf

def test_invalid_input():
    with patch('pytutils.pretty._pprint', None):
        # Test case for invalid input, e.g., passing a non-string or non-serializable object
        with pytest.raises(AttributeError):
            result = pf([1, 2, {'key': 'value'}])
