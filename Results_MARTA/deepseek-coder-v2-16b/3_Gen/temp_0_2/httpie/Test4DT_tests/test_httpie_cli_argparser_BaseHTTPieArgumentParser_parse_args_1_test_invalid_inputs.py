
import pytest
from httpie.cli.argparser import BaseHTTPieArgumentParser
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    parser = BaseHTTPieArgumentParser()
    
    with patch('httpie.cli.argparser.Environment', autospec=True) as mock_env:
        mock_env.stdin = None
        
        # Test invalid inputs
        with pytest.raises(AttributeError):
            result = parser.parse_args(env=mock_env, args=['--invalid-option'])
