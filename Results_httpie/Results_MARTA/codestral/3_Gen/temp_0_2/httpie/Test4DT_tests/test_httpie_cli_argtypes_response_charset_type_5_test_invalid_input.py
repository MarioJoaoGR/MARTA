
import pytest
from httpie.cli.argtypes import response_charset_type
import argparse
from unittest.mock import patch

def test_invalid_input():
    with pytest.raises(argparse.ArgumentTypeError):
        with patch('httpie.cli.argtypes.response_charset_type', side_effect=LookupError):
            response_charset_type('unknown_encoding')
