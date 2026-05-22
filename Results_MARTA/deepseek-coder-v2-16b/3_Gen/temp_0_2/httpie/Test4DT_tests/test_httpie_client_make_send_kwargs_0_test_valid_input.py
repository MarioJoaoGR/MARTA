
import argparse
from httpie.client import make_send_kwargs
import pytest
from unittest.mock import patch, MagicMock

def test_valid_input():
    # Create a mock argparse Namespace object with timeout set to 5.0
    args = argparse.Namespace(timeout=5.0)
    
    # Call the function and check the output
    send_kwargs = make_send_kwargs(args)
    assert send_kwargs == {'timeout': 5.0, 'allow_redirects': False}
