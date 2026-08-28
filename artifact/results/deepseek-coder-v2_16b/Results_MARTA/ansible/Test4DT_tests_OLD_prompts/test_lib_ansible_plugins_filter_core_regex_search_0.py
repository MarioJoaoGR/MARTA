
import pytest
from ansible.plugins.filter.core import regex_search
import re
from unittest.mock import patch

def test_regex_search_basic():
    with patch('ansible.plugins.filter.core.re.search') as mock_search:
        # Mock the search function to return a match object
        mock_match = mock_search.return_value = type('', (), {'group': lambda x: 'matched'})()
        
        result = regex_search('hello world', r'world')
        assert result == 'matched'

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=native"])
