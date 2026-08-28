
import pytest
from unittest.mock import patch, MagicMock
import requests
from httpie.client import HTTPieHTTPSAdapter
from httpie_https_adapter import build_requests_session

def test_valid_inputs():
    with patch('httpie.client.HTTPieHTTPSAdapter', autospec=True):
        session = build_requests_session(verify=True, ssl_version='TLSv1.2', ciphers='ECDHE-RSA-AES256-GCM-SHA384')
        
        assert isinstance(session, requests.Session)
        assert len(session.adapters) == 2
        assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
        assert session.adapters['https://'].verify == True
        assert session.adapters['https://'].ssl_version == 'TLSv1.2'
        assert session.adapters['https://'].ciphers == 'ECDHE-RSA-AES256-GCM-SHA384'

def test_default_inputs():
    with patch('httpie.client.HTTPieHTTPSAdapter', autospec=True):
        session = build_requests_session(verify=False)
        
        assert isinstance(session, requests.Session)
        assert len(session.adapters) == 2
        assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
        assert session.adapters['https://'].verify == False
        assert session.adapters['https://'].ssl_version is None
        assert session.adapters['https://'].ciphers is None

def test_invalid_ssl_version():
    with patch('httpie.client.HTTPieHTTPSAdapter', autospec=True):
        with pytest.raises(ValueError):
            build_requests_session(verify=True, ssl_version='INVALID_SSL_VERSION')

def test_missing_ssl_version():
    with patch('httpie.client.HTTPieHTTPSAdapter', autospec=True):
        session = build_requests_session(verify=True)
        
        assert isinstance(session, requests.Session)
        assert len(session.adapters) == 2
        assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
        assert session.adapters['https://'].verify == True
        assert session.adapters['https://'].ssl_version is None
        assert session.adapters['https://'].ciphers is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_httpie_client_build_requests_session_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_build_requests_session_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_build_requests_session_0.py:6: in <module>
    from httpie_https_adapter import build_requests_session
E   ModuleNotFoundError: No module named 'httpie_https_adapter'
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_build_requests_session_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.78s ==========================
"""