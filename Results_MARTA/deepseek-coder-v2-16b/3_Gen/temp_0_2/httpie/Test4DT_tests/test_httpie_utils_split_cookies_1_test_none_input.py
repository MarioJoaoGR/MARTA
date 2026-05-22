
import pytest
from unittest.mock import patch
from httpie.utils import split_cookies

def test_none_input():
    with patch('httpie.utils.RE_COOKIE_SPLIT', create=True) as mock_re_cookie_split:
        mock_re_cookie_split.return_value = lambda x: x.split(', ')
        
        assert split_cookies(None) == []
