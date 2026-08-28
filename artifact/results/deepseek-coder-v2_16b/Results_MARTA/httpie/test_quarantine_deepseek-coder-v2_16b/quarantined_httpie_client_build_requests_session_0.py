
import pytest
import requests
from httpie_https_adapter import HTTPieHTTPSAdapter

def build_requests_session(verify, ssl_version=None, ciphers=None):
    session = requests.Session()
    adapter = HTTPieHTTPSAdapter(ciphers=ciphers, verify=verify, ssl_version=ssl_version)
    session.mount('https://', adapter)
    return session

def test_build_requests_session_default():
    session = build_requests_session(verify=True)
    assert isinstance(session, requests.Session), "Expected a requests.Session object"
    assert len(session.adapters) == 1, "Expected one adapter to be mounted"
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter), "Expected the adapter to be HTTPieHTTPSAdapter"

def test_build_requests_session_with_ssl_version():
    session = build_requests_session(verify=True, ssl_version='TLSv1.2')
    assert isinstance(session, requests.Session), "Expected a requests.Session object"
    assert len(session.adapters) == 1, "Expected one adapter to be mounted"
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter), "Expected the adapter to be HTTPieHTTPSAdapter"
    assert session.adapters['https://'].ssl_version == 'TLSv1.2', "Expected SSL version to be TLSv1.2"

def test_build_requests_session_with_ciphers():
    session = build_requests_session(verify=True, ciphers='ECDHE-RSA-AES256-GCM-SHA384')
    assert isinstance(session, requests.Session), "Expected a requests.Session object"
    assert len(session.adapters) == 1, "Expected one adapter to be mounted"
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter), "Expected the adapter to be HTTPieHTTPSAdapter"
    assert session.adapters['https://'].ciphers == 'ECDHE-RSA-AES256-GCM-SHA384', "Expected ciphers to be ECDHE-RSA-AES256-GCM-SHA384"

def test_build_requests_session_disable_ssl_verification():
    session = build_requests_session(verify=False)
    assert isinstance(session, requests.Session), "Expected a requests.Session object"
    assert len(session.adapters) == 1, "Expected one adapter to be mounted"
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter), "Expected the adapter to be HTTPieHTTPSAdapter"
    assert not session.adapters['https://'].verify, "Expected SSL verification to be disabled"

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
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_build_requests_session_0.py:4: in <module>
    from httpie_https_adapter import HTTPieHTTPSAdapter
E   ModuleNotFoundError: No module named 'httpie_https_adapter'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_build_requests_session_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.21s ===============================
"""