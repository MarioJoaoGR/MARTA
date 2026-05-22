
import pytest
from unittest.mock import patch
from httpie.ssl_ import HTTPieHTTPSAdapter

def test_invalid_inputs():
    with pytest.raises(Exception):
        adapter = HTTPieHTTPSAdapter(verify='invalid', ssl_version='invalid', ciphers='invalid')
