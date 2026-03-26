
import pytest
from unittest.mock import patch
from superstring.superstring import SuperStringLower

def test_edge_case_none():
    with patch('builtins.print') as mock_print:
        s = SuperStringLower(None)
        assert s._base is None
        with pytest.raises(AttributeError):
            s.upper()
