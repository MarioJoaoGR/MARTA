
import argparse
from unittest import mock
import pytest
from httpie.client import make_send_kwargs_mergeable_from_env, HTTPieCertificate

class TestMakeSendKwargsMergeableFromEnv:
    def test_valid_inputs(self):
        # Define the arguments for the function
        args = argparse.Namespace()
        args.cert = "path/to/cert"
        args.cert_key = "path/to/cert_key"
        args.cert_key_pass = mock.Mock()
        args.cert_key_pass.value = "passphrase"
        args.proxy = [mock.Mock(key="http", value="http://proxy"), mock.Mock(key="https", value="https://proxy")]
        args.verify = "yes"
    
        # Call the function with the defined arguments
        send_kwargs = make_send_kwargs_mergeable_from_env(args)
    
        # Assert that the returned dictionary has the expected values
        assert send_kwargs['proxies'] == {'http': 'http://proxy', 'https': 'https://proxy'}
        assert send_kwargs['stream'] is True
        assert send_kwargs['verify'] is True
        assert send_kwargs['cert'] == HTTPieCertificate("path/to/cert", "path/to/cert_key", "passphrase")
