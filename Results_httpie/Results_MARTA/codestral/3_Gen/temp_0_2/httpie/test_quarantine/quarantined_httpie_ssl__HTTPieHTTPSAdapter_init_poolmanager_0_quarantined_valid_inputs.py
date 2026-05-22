
import pytest
from unittest.mock import patch, MagicMock
from httpie.ssl_ import HTTPieHTTPSAdapter

@pytest.fixture
def valid_inputs():
    return {'ciphers': 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384', 'ssl_version': 'TLSv1.2', 'verify': True}

def test_valid_inputs(valid_inputs):
    with patch('httpie.ssl_.HTTPieHTTPSAdapter._create_ssl_context', return_value=MagicMock()):
        adapter = HTTPieHTTPSAdapter(**valid_inputs)
        assert hasattr(adapter, '_ssl_context')
        assert isinstance(adapter._ssl_context, MagicMock)
        poolmanager = adapter.init_poolmanager()
        assert poolmanager is not None

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

httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

valid_inputs = {'ciphers': 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384', 'ssl_version': 'TLSv1.2', 'verify': True}

    def test_valid_inputs(valid_inputs):
        with patch('httpie.ssl_.HTTPieHTTPSAdapter._create_ssl_context', return_value=MagicMock()):
            adapter = HTTPieHTTPSAdapter(**valid_inputs)
            assert hasattr(adapter, '_ssl_context')
            assert isinstance(adapter._ssl_context, MagicMock)
>           poolmanager = adapter.init_poolmanager()

httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_valid_inputs.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.ssl_.HTTPieHTTPSAdapter object at 0x7febb92ba8d0>, args = ()
kwargs = {'ssl_context': <MagicMock id='140650398851088'>}

    def init_poolmanager(self, *args, **kwargs):
        kwargs['ssl_context'] = self._ssl_context
>       return super().init_poolmanager(*args, **kwargs)
E       TypeError: HTTPAdapter.init_poolmanager() missing 2 required positional arguments: 'connections' and 'maxsize'

httpie/httpie/ssl_.py:57: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.20s ===============================
"""