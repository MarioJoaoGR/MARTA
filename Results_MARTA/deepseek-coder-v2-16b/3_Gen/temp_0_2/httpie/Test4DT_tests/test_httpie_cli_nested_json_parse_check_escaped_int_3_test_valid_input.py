
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.parse import check_escaped_int, BACKSLASH

def test_valid_input():
    with patch('builtins.print'):  # Mocking print to avoid actual output in tests
        assert check_escaped_int(r'\123') == '123'
