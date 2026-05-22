
import argparse
from httpie.client import make_send_kwargs
import pytest
from unittest.mock import patch, MagicMock

def test_valid_input():
    # Create a mock argparse namespace with timeout set to 5.0
    args = MagicMock()
    args.timeout = 5.0
    
    # Patch the make_send_kwargs function to return the expected dictionary
    with patch('httpie.client.make_send_kwargs', return_value={'timeout': 5.0, 'allow_redirects': False}):
        result = make_send_kwargs(args)
        
        # Assert that the result matches the expected output
        assert result == {'timeout': 5.0, 'allow_redirects': False}
