
import pytest
from unittest.mock import patch, MagicMock
from httpie.client import build_requests_session
import requests

def test_invalid_inputs():
    with patch('httpie.client.HTTPieHTTPSAdapter', autospec=True):
        with pytest.raises(KeyError):
            build_requests_session(verify=False, ssl_version='TLSv1.2', ciphers='ECDHE-RSA-AES256-GCM-SHA384')
