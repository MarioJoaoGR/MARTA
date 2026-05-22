
import pytest
from unittest.mock import patch
from httpie.ssl_ import HTTPieHTTPSAdapter

@pytest.fixture(name="valid_inputs")
def fixture_valid_inputs():
    return {
        "verify": True,
        "ssl_version": 'TLSv1.2',
        "ciphers": 'ECDHE-RSA-AES256-GCM-SHA384'
    }

@pytest.fixture(name="adapter")
def fixture_adapter(valid_inputs):
    return HTTPieHTTPSAdapter(**valid_inputs)

def test_httpie_https_adapter(adapter, valid_inputs):
    with patch('httpie.ssl_.HTTPieHTTPSAdapter._create_ssl_context', autospec=True) as mock_create_ssl_context:
        adapter = HTTPieHTTPSAdapter(**valid_inputs)
        assert isinstance(adapter._ssl_context, type(mock_create_ssl_context.return_value))
        assert adapter.verify == valid_inputs["verify"]
        assert adapter.ssl_version == valid_inputs["ssl_version"]
        assert adapter.ciphers == valid_inputs["ciphers"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_1_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_1_test_valid_inputs.py:22:15: E1101: Instance of 'HTTPieHTTPSAdapter' has no 'verify' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_1_test_valid_inputs.py:23:15: E1101: Instance of 'HTTPieHTTPSAdapter' has no 'ssl_version' member (no-member)
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_1_test_valid_inputs.py:24:15: E1101: Instance of 'HTTPieHTTPSAdapter' has no 'ciphers' member (no-member)


"""