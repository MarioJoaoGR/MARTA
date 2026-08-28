
import pytest
from unittest.mock import patch
from sanic.headers import fwd_normalize_address



def test_valid_input_obfuscated_string():
    with patch('sanic.headers._ipv6_re', None):  # Mocking _ipv6_re for simplicity
        normalized_addr = fwd_normalize_address("_hiddenvalue")
        assert normalized_addr == "_hiddenvalue"

def test_invalid_input_unknown():
    with pytest.raises(ValueError):
        fwd_normalize_address("unknown")