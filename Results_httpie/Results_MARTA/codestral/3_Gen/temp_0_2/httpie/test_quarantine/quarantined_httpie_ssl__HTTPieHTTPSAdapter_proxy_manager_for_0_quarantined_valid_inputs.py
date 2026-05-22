
import unittest
from httpie.ssl_ import create_default_context
from unittest.mock import patch, MagicMock

class HTTPieHTTPSAdapter(HTTPieHTTPSAdapter):
    def __init__(self, verify: bool, ssl_version: str = None, ciphers: str = None, **kwargs):
        self._ssl_context = self._create_ssl_context(verify=verify, ssl_version=ssl_version, ciphers=ciphers)
        super().__init__(**kwargs)

    def _create_ssl_context(self, verify: bool, ssl_version: str, ciphers: str):
        context = create_default_context()
        if verify:
            context.check_hostname = False
            context.verify_mode = ssl.CERT_REQUIRED
        else:
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
        
        if ssl_version:
            context.ssl_version = getattr(ssl, ssl_version)
        if ciphers:
            context.ciphers = ciphers
        return context

    def proxy_manager_for(self, *args, **kwargs):
        kwargs['ssl_context'] = self._ssl_context
        return super().proxy_manager_for(*args, **kwargs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_valid_inputs.py:3:0: E0611: No name 'create_default_context' in module 'httpie.ssl_' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_valid_inputs.py:6:25: E0602: Undefined variable 'HTTPieHTTPSAdapter' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_valid_inputs.py:15:34: E0602: Undefined variable 'ssl' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_valid_inputs.py:18:34: E0602: Undefined variable 'ssl' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_valid_inputs.py:21:42: E0602: Undefined variable 'ssl' (undefined-variable)


"""