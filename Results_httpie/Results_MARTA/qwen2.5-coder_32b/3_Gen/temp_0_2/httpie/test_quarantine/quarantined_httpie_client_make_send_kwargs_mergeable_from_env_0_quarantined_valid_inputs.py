
import argparse
from unittest.mock import patch, MagicMock
from httpie.client import make_send_kwargs_mergeable_from_env, HTTPieCertificate

def test_make_send_kwargs_mergeable_from_env():
    mock_args = argparse.Namespace(
        cert='path/to/cert',
        cert_key='path/to/cert_key',
        cert_key_pass=MagicMock(value='passphrase'),
        proxy=[MagicMock(key='http', value='http://proxy'), MagicMock(key='https', value='https://proxy')],
        verify='yes'
    )
    
    with patch('httpie.client.HTTPieCertificate', autospec=True) as mock_cert:
        result = make_send_kwargs_mergeable_from_env(mock_args)
        
        assert 'proxies' in result
        assert result['proxies'] == {'http': 'http://proxy', 'https': 'https://proxy'}
        assert result['stream'] is True
        assert result['verify'] is True
        assert result['cert'] == "path/to/cert"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_make_send_kwargs_mergeable_from_env_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
___________________ test_make_send_kwargs_mergeable_from_env ___________________

    def test_make_send_kwargs_mergeable_from_env():
        mock_args = argparse.Namespace(
            cert='path/to/cert',
            cert_key='path/to/cert_key',
            cert_key_pass=MagicMock(value='passphrase'),
            proxy=[MagicMock(key='http', value='http://proxy'), MagicMock(key='https', value='https://proxy')],
            verify='yes'
        )
    
        with patch('httpie.client.HTTPieCertificate', autospec=True) as mock_cert:
            result = make_send_kwargs_mergeable_from_env(mock_args)
    
            assert 'proxies' in result
            assert result['proxies'] == {'http': 'http://proxy', 'https': 'https://proxy'}
            assert result['stream'] is True
            assert result['verify'] is True
>           assert result['cert'] == "path/to/cert"
E           AssertionError: assert <NonCallableMagicMock name='HTTPieCertificate()' spec='HTTPieCertificate' id='140493293861264'> == 'path/to/cert'

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_make_send_kwargs_mergeable_from_env_0_test_valid_inputs.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_make_send_kwargs_mergeable_from_env_0_test_valid_inputs.py::test_make_send_kwargs_mergeable_from_env
============================== 1 failed in 0.24s ===============================
"""