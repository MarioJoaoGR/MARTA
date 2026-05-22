
import sys
from unittest.mock import patch
from httpie.uploads import is_stdin

def test_error_handling():
    with patch('sys.stdin', create=True) as mock_stdin:
        # Mock the fileno method to return a specific value for testing
        mock_stdin.fileno.return_value = 0
        
        assert is_stdin(mock_stdin) == True
