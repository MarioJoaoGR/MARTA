
import pytest
from httpie.utils import get_expired_cookies
from unittest.mock import patch, MagicMock

def test_invalid_input():
    with patch('httpie.utils.time.time', return_value=1672502400):  # Example timestamp for testing
        expired_cookies = get_expired_cookies('cookie1=value1; Max-Age=3600, cookie2=value2; Expires=1672502400')
        assert len(expired_cookies) == 0
