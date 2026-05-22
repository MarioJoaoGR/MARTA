
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import process_header_arg, KeyValueArg

def test_none_input():
    with patch('httpie.cli.requestitems.KeyValueArg', autospec=True) as mock_keyvaluearg:
        mock_keyvaluearg.return_value.value = None
        assert process_header_arg(mock_keyvaluearg.return_value) is None
