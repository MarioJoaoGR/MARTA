
import pytest
from unittest.mock import patch
from youtube_dl.extractor.safari import SafariBaseIE
from youtube_dl.compat import compat_urlparse, compat_parse_qs
import json

# Test for valid login credentials

# Test for invalid login credentials
def test_invalid_credentials():
    with patch('youtube_dl.extractor.safari.SafariBaseIE._get_login_info', return_value=('invaliduser', 'invalidpass')):
        safari_ie = SafariBaseIE()
        assert not safari_ie.LOGGED_IN
        with pytest.raises(Exception):  # Assuming ExtractorError is the exception raised on login failure
            safari_ie._login()