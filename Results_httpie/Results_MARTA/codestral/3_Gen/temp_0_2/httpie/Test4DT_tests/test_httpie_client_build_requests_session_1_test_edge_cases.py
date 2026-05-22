
import pytest
from unittest.mock import patch, MagicMock
import requests
from httpie.client import build_requests_session

def test_build_requests_session():
    with patch('httpie.client.HTTPieHTTPSAdapter') as mock_adapter:
        session = build_requests_session(verify=True)

        assert isinstance(session, requests.Session)
        assert len(session.adapters) == 2
        assert 'http://' in session.adapters
        assert 'https://' in session.adapters

        http_adapter = session.adapters['http://']
        https_adapter = session.adapters['https://']

        assert isinstance(http_adapter, requests.adapters.HTTPAdapter)
        assert isinstance(https_adapter, MagicMock)
        assert hasattr(mock_adapter, 'called')
