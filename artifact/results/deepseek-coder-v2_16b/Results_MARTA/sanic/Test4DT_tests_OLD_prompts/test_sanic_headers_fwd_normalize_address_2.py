
import pytest
from unittest.mock import patch
from sanic.headers import fwd_normalize_address


def test_obfuscated_string():
    with patch('sanic.headers._ipv6_re', return_value=False):
        assert fwd_normalize_address("_hiddenvalue") == "_hiddenvalue"

def test_unknown_address():
    with pytest.raises(ValueError):
        fwd_normalize_address("unknown")
