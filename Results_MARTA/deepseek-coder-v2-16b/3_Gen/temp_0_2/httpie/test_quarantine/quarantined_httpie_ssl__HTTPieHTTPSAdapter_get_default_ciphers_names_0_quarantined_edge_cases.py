
import ssl
from unittest.mock import patch, MagicMock
import pytest

class HTTPieHTTPSAdapter:
    def __init__(self, verify: bool, ssl_version: str = None, ciphers: str = None, **kwargs):
        self._ssl_context = self._create_ssl_context(verify=verify, ssl_version=ssl_version, ciphers=ciphers)
        super().__init__(**kwargs)

    @classmethod
    def get_default_ciphers_names(cls):
        return [cipher['name'] for cipher in cls._create_ssl_context(verify=False).get_ciphers()]

    @staticmethod
    def _create_ssl_context(verify, ssl_version, ciphers):
        context = ssl.create_default_context()
        if verify:
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
        if ssl_version:
            context.set_ciphers(ssl_version)
        elif ciphers:
            context.set_ciphers(ciphers)
        return context

@pytest.mark.parametrize("input_value, expected", [
    (None, []),
    ("", [])
])
def test_edge_cases(input_value, expected):
    with patch('httpie.ssl_.HTTPieHTTPSAdapter._create_ssl_context', return_value=MagicMock()):
        assert HTTPieHTTPSAdapter.get_default_ciphers_names() == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_edge_cases.py:13:45: E1120: No value for argument 'ssl_version' in staticmethod call (no-value-for-parameter)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_edge_cases.py:13:45: E1120: No value for argument 'ciphers' in staticmethod call (no-value-for-parameter)


"""