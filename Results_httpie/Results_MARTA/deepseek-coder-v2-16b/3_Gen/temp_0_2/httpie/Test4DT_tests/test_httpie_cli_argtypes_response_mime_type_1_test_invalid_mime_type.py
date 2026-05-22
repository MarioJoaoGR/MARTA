
import pytest
from httpie.cli.argtypes import response_mime_type
import argparse
from unittest.mock import patch

def test_invalid_mime_type():
    with pytest.raises(argparse.ArgumentTypeError):
        with patch('httpie.cli.argtypes.response_mime_type', side_effect=response_mime_type):
            response_mime_type('invalid-mime-type')
