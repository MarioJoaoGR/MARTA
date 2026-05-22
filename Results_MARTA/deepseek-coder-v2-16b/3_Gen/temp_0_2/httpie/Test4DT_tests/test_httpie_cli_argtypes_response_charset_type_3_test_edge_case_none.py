
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

@pytest.mark.parametrize("input_encoding, expected", [
    (None, TypeError),  # Test for None input
])
def test_edge_case_none(input_encoding, expected):
    with pytest.raises(expected):
        response_charset_type(input_encoding)
