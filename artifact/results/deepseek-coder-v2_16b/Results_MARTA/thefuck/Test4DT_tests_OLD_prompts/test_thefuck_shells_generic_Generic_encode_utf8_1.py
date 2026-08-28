
import pytest
from unittest.mock import patch
from thefuck.shells.generic import Generic

def test_encode_utf8_with_py2():
    generic_shell = Generic()
    with patch('six.PY2', True):
        result = generic_shell.encode_utf8("This is a test command.")
        assert isinstance(result, bytes)
        assert result == b"This is a test command."

def test_encode_utf8_with_py3():
    generic_shell = Generic()
    with patch('six.PY2', False):
        result = generic_shell.encode_utf8("This is a test command.")
        assert isinstance(result, str)
        assert result == "This is a test command."
