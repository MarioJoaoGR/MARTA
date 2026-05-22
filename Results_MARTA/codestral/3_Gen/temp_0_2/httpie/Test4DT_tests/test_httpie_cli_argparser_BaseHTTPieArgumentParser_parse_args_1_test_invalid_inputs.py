
import pytest
from httpie.cli.argparser import BaseHTTPieArgumentParser
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    parser = BaseHTTPieArgumentParser()
    
    with patch('httpie.cli.argparser.Environment', autospec=True) as mock_env:
        # Create a mock environment object with stdin and isatty attributes
        mock_env.return_value.stdin = True
        mock_env.return_value.stdin_isatty = False
        
        # Test invalid inputs by passing None to parse_args method
        with pytest.raises(AttributeError):
            parser.parse_args(env=mock_env.return_value, args=['--invalid-option'])
