
import pytest
from httpie.ssl_ import HTTPieHTTPSAdapter, resolve_ssl_version
from unittest.mock import patch
import ssl

@pytest.fixture
def setup_httpie_https_adapter():
    with patch('httpie.ssl_.resolve_ssl_version', return_value=ssl.PROTOCOL_TLS):
        return HTTPieHTTPSAdapter(verify=True, ssl_version='TLSv1.2', ciphers='ECDHE-RSA-AES256-GCM-SHA384')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
============================ no tests ran in 0.16s =============================
"""