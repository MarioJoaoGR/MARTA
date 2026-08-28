
import re
from ansible.plugins.filter.core import regex_escape
import pytest
from unittest.mock import patch

# Test for basic functionality of regex_escape with default 'python' type
def test_regex_escape_basic():
    with patch('ansible.plugins.filter.core.re.escape') as mock_re_escape:
        mock_re_escape.return_value = "Escaped"
        
        result = regex_escape("Hello, World!")
        
        assert result == "Escaped"
        mock_re_escape.assert_called_once_with("Hello, World!")
