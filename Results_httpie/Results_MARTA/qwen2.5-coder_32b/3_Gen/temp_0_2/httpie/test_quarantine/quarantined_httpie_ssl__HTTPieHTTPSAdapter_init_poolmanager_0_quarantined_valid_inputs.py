
import pytest
from httpie.ssl_ import HTTPieHTTPSAdapter, resolve_ssl_version, PROTOCOL_TLS
from unittest.mock import patch

@pytest.fixture
def valid_inputs():
    return {'ciphers': 'ECDHE-RSA-AES256-GCM-SHA384', 'ssl_version': 'TLSv1.2', 'verify': True}

@pytest.fixture
def httpie_https_adapter(valid_inputs):
    with patch('httpie.ssl_.resolve_ssl_version') as mock_resolve:
        mock_resolve.return_value = PROTOCOL_TLS
        return HTTPieHTTPSAdapter(**valid_inputs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_valid_inputs.py:3:0: E0611: No name 'PROTOCOL_TLS' in module 'httpie.ssl_' (no-name-in-module)


"""