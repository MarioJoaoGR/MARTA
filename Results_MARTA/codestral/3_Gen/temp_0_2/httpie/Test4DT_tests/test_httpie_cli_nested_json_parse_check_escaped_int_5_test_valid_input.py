
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.parse import check_escaped_int, BACKSLASH

def test_valid_input():
    with patch('builtins.print'):  # Mocking print to avoid actual output in tests
        with pytest.raises(ValueError) as exc_info:
            assert check_escaped_int('\123') == '123'
    assert str(exc_info.value) == "Not an escaped int"
