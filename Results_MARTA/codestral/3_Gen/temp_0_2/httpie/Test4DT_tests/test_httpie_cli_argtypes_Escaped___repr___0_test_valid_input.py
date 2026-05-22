
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import Escaped

def test_valid_input():
    with patch('httpie.cli.argtypes.Escaped.__repr__', return_value="Escaped('\\x00')"):
        escaped_instance = Escaped()
        assert repr(escaped_instance) == "Escaped('\\x00')"
