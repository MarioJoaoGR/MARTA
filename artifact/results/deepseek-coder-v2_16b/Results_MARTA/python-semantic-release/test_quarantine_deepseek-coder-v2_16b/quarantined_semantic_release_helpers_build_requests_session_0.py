
import pytest
from requests import Session, Retry
from semantic_release.helpers import build_requests_session

def test_build_requests_session_default():
    session = build_requests_session()
    assert isinstance(session, Session)
    assert hasattr(session, 'hooks')
    assert 'response' in session.hooks
    assert callable(session.hooks['response'][0])

def test_build_requests_session_with_raise_for_status():
    session = build_requests_session(raise_for_status=True)
    assert isinstance(session, Session)
    assert hasattr(session, 'hooks')
    assert 'response' in session.hooks
    assert callable(session.hooks['response'][0])
    with pytest.raises(Exception):
        response = session.get('http://invalid-url')
        response.raise_for_status()

def test_build_requests_session_with_retry():
    retry = Retry(total=2, backoff_factor=0.5)
    session = build_requests_session(retry=retry)
    assert isinstance(session, Session)
    adapter = session.adapters['http://']
    assert isinstance(adapter, HTTPAdapter)
    assert hasattr(adapter, 'max_retries')
    assert adapter.max_retries == retry

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__ ERROR collecting test_semantic_release_helpers_build_requests_session_0.py __
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_build_requests_session_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_build_requests_session_0.py:3: in <module>
    from requests import Session, Retry
E   ImportError: cannot import name 'Retry' from 'requests' (/data/pydeps/marta/requests/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_build_requests_session_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""