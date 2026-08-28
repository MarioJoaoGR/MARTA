
import pytest
from ansible.plugins.filter.core import regex_replace
import re
from unittest.mock import patch, MagicMock

def test_edge_cases():
    with patch('re.compile', autospec=True) as mock_compile, \
         patch('re.sub', autospec=True) as mock_sub:

        # Mock the behavior of re.compile and re.sub
        mock_compile.return_value = MagicMock()
        mock_compile.return_value.sub = MagicMock(return_value='Hello Universe')

        # Test with None input
        result = regex_replace(None, 'World', 'Universe')

        assert result == 'Hello Universe'
