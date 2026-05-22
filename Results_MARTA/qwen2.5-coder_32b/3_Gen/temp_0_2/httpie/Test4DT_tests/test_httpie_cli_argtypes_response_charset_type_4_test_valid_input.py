
import pytest
from unittest.mock import patch
import argparse

def response_charset_type(encoding: str) -> str:
    try:
        ''.encode(encoding)
    except LookupError:
        raise argparse.ArgumentTypeError(
            f'{encoding!r} is not a supported encoding')
    return encoding

@pytest.mark.parametrize("valid_encoding", ['utf-8', 'ascii'])
def test_valid_input(valid_encoding):
    with patch('builtins.__import__', return_value=lambda *args, **kwargs: None):
        assert response_charset_type(valid_encoding) == valid_encoding
