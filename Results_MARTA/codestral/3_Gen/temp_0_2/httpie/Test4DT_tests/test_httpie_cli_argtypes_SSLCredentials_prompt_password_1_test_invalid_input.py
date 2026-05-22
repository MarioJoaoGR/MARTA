
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import SSLCredentials

def test_invalid_input():
    with patch('builtins.input', return_value=''):
        ssl_credentials = SSLCredentials(value='')
        assert ssl_credentials.value == ''
