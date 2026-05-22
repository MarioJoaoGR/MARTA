
import pytest
from httpie.cli.argtypes import response_mime_type
import argparse
from unittest.mock import patch

def test_valid_mime_type():
    with patch('httpie.cli.argtypes.response_mime_type', side_effect=lambda x: x):
        assert response_mime_type('text/plain') == 'text/plain'
        assert response_mime_type('application/json') == 'application/json'
        assert response_mime_type('multipart/form-data') == 'multipart/form-data'
