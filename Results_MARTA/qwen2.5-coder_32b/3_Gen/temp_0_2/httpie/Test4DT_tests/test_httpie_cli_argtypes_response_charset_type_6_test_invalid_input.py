
import pytest
from httpie.cli.argtypes import response_charset_type
import argparse

def test_invalid_input():
    with pytest.raises(argparse.ArgumentTypeError):
        response_charset_type('unknown_encoding')
