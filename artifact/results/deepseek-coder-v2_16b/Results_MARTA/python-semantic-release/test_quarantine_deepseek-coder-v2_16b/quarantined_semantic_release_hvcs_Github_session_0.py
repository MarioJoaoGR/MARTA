
import pytest
from semantic_release.hvcs import Github
from requests import Session, Retry
from unittest.mock import patch

def build_requests_session(raise_for_status=True, retry=None):
    session = Session()
    if raise_for_status:
        session.hooks['response'] = [lambda r, *args, **kwargs: r.raise_for_status()]
    if retry:
        if isinstance(retry, bool) and retry:
            retry = Retry(total=5, backoff_factor=0.1)
        elif isinstance(retry, int):
            retry = Retry(total=retry, backoff_factor=0.1)
        session.mount('https://', RetryAdapter(max_retries=retry))
    return session

class RetryAdapter:
    def __init__(self, max_retries):
        self.max_retries = max_retries

    def send(self, request, **kwargs):
        import requests
        retries = 0
        while True:
            try:
                response = requests.Session().send(request, **kwargs)
                return response
            except requests.RequestException as e:
                if retries >= self.max_retries:
                    raise e
                retries += 1
                time.sleep(0.1 * (2 ** retries))

def test_default_session():
    session = Github.session()
    assert isinstance(session, Session)

@pytest.mark.parametrize("raise_for_status, retry", [
    (False, True),
    (True, False),
    (True, 3),
])
def test_customized_sessions(raise_for_status, retry):
    session = Github.session(raise_for_status=raise_for_status, retry=retry)
    assert isinstance(session, Session)
    if raise_for_status:
        with pytest.raises(requests.HTTPError):
            session.get('http://invalid-url')
    else:
        response = session.get('http://invalid-url')
        assert not response.raise_for_status()

@patch('semantic_release.hvcs.Github.auth', return_value='fake_token')
def test_session_with_env_token(mock_auth):
    session = Github.session()
    mock_auth.assert_called_once()
    assert isinstance(session, Session)
    assert session.auth == 'fake_token'

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
_______ ERROR collecting test_semantic_release_hvcs_Github_session_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_session_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_session_0.py:4: in <module>
    from requests import Session, Retry
E   ImportError: cannot import name 'Retry' from 'requests' (/data/pydeps/marta/requests/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_session_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.22s ===============================
"""