
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

@pytest.mark.parametrize("valid_input, expected", [
    ('utf-8', 'utf-8'),
    ('ascii', 'ascii')
])
def test_valid_input(valid_input, expected):
    with patch('argparse.ArgumentTypeError', side_effect=None):  # Mocking to avoid raising ArgumentTypeError
        assert response_charset_type(valid_input) == expected
