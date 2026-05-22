
import pytest
from httpie.utils import url_as_host
from urllib.parse import urlsplit
from unittest.mock import patch

def test_invalid_input():
    with patch('httpie.utils.urlsplit') as mock_urlsplit:
        # Mock the urlsplit to raise ValueError for invalid input
        mock_urlsplit.side_effect = ValueError("Invalid URL")
        
        # Test that url_as_host raises Exception when given an invalid input
        with pytest.raises(Exception):
            url_as_host('invalid-url')
