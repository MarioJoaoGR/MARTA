
import pytest
from httpie.cli.argparser import BaseHTTPieArgumentParser
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    parser = BaseHTTPieArgumentParser()
    
    with patch('httpie.cli.argparser.Environment', autospec=True) as mock_env:
        # Create a mock environment object
        env = mock_env.return_value
        env.stdin = None  # Set stdin to None for testing invalid input
        
        # Call the parse_args method with invalid inputs
        with pytest.raises(AttributeError):
            parser.parse_args(env=env, args=['--invalid-option'])
