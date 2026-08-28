
import pytest
from unittest.mock import patch
from youtube_dl.extractor.safari import SafariBaseIE

def test_valid_login():
    with patch('youtube_dl.extractor.safari.SafariBaseIE._login') as mock_login:
        safari_ie = SafariBaseIE()
        safari_ie._real_initialize()  # This will trigger _login method
        assert mock_login.call_count == 1, "Expected '_login' to have been called once."

def test_missing_netrc():
    with pytest.raises(TypeError):
        SafariBaseIE(netrc=False)

def test_invalid_credentials():
    with pytest.raises(TypeError):
        SafariBaseIE(valid_creds=False)
