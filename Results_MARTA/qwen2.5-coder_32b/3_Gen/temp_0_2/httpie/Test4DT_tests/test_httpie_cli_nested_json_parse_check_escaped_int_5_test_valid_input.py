
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.parse import check_escaped_int

def test_valid_input():
    with patch('httpie.cli.nested_json.parse.check_escaped_int', return_value='123'):
        result = check_escaped_int("\\123")
        assert result == '123'
