
from unittest.mock import patch, MagicMock
import pytest
from thefuck.shells.generic import Generic

def test_quote_with_none():
    generic = Generic()
    with patch('thefuck.shells.generic.Generic.quote', side_effect=Exception("Invalid input")):
        with pytest.raises(Exception):
            assert generic.quote(None)

def test_quote_with_empty_string():
    generic = Generic()
    with patch('thefuck.shells.generic.Generic.quote', return_value=''):
        assert generic.quote("") == ""
