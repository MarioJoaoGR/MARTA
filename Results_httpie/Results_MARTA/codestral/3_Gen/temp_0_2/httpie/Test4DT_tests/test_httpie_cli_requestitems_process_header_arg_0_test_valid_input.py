
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import KeyValueArg, process_header_arg

def test_valid_input():
    with patch('httpie.cli.requestitems.KeyValueArg', autospec=True) as mock_keyvaluearg:
        mock_instance = mock_keyvaluearg.return_value
        mock_instance.value = 'Content-Type'
        
        result = process_header_arg(mock_instance)
        
        assert result == 'Content-Type'
