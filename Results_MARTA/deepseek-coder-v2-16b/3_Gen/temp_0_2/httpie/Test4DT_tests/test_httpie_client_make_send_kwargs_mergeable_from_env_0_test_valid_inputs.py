
import argparse
from unittest.mock import patch
import pytest
from httpie.client import make_send_kwargs_mergeable_from_env

@pytest.fixture
def mock_args():
    args = argparse.Namespace(
        cert="cert_path",
        cert_key="cert_key_path",
        cert_key_pass=argparse.Namespace(value="passphrase"),
        proxy=[argparse.Namespace(key="proxy_key", value="proxy_value")],
        verify="yes"
    )
    return args

def test_make_send_kwargs_mergeable_from_env(mock_args):
    with patch('httpie.client.HTTPieCertificate', autospec=True) as mock_cert:
        result = make_send_kwargs_mergeable_from_env(mock_args)
        
        assert 'proxies' in result
        assert result['proxies'] == {'proxy_key': 'proxy_value'}
        assert result['stream'] is True
        assert result['verify'] is True
        assert result['cert'] is not None
        mock_cert.assert_called_once_with("cert_path", "cert_key_path", "passphrase")
