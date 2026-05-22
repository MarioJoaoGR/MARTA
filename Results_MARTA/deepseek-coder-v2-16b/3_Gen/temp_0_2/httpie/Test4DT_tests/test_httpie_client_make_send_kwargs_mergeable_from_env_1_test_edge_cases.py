
import argparse
from unittest.mock import patch, MagicMock
import pytest
from httpie.client import make_send_kwargs_mergeable_from_env

@pytest.fixture
def mock_args():
    args = argparse.Namespace(
        cert='cert_path',
        cert_key='cert_key_path',
        cert_key_pass=argparse.Namespace(value='passphrase'),
        proxy=[MagicMock(key='proxy_key1', value='proxy_value1'), MagicMock(key='proxy_key2', value='proxy_value2')],
        verify='yes'
    )
    return args

def test_make_send_kwargs_mergeable_from_env(mock_args):
    with patch('httpie.client.HTTPieCertificate', autospec=True) as mock_cert:
        result = make_send_kwargs_mergeable_from_env(mock_args)
        
        assert 'proxies' in result
        assert result['proxies'] == {'proxy_key1': 'proxy_value1', 'proxy_key2': 'proxy_value2'}
        assert result['stream'] is True
        assert result['verify'] is True
        assert result['cert'] == mock_cert.return_value
