
import pytest
from httpie.compat import ensure_default_certs_loaded
from ssl import SSLContext
from unittest.mock import patch, MagicMock

@pytest.fixture(name="valid_sslcontext")
def fixture_valid_sslcontext():
    with patch('httpie.compat.ensure_default_certs_loaded') as mock_load:
        ssl_context = SSLContext()
        yield ssl_context
        # Ensure that the function was called and check the result
        assert mock_load.called
        assert hasattr(ssl_context, 'load_default_certs')
        assert ssl_context.get_ca_certs() != []  # Ensure default certs are loaded

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
report saved to: pytest_report_codestral.json
============================ no tests ran in 0.04s =============================
"""