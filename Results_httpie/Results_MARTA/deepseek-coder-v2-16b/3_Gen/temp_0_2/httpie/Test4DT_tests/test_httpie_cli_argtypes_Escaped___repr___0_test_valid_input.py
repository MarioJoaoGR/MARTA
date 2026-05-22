
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import Escaped

def test_valid_input():
    escaped = Escaped()
    with patch('httpie.cli.argtypes.Escaped.__repr__', return_value="MockedRepr"):
        assert repr(escaped) == "MockedRepr"
