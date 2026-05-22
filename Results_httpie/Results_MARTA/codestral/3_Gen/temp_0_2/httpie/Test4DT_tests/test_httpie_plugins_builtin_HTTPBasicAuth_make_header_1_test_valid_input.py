
import pytest
from unittest.mock import patch
from httpie.plugins.builtin import HTTPBasicAuth

def test_valid_input():
    with patch('httpie.plugins.builtin.HTTPBasicAuth.make_header', return_value='Basic dXNlcjpwYXNz'):
        result = HTTPBasicAuth.make_header('user', 'pass')
        assert result == 'Basic dXNlcjpwYXNz'
