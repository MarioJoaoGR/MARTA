
import pytest
from httpie.sessions import Session


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_auth_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_auth ________________________________

    def test_valid_auth():
        session = Session(path='fake_path')
        session['auth'] = {'type': 'basic', 'raw_auth': 'username:password'}
    
        assert session['auth']['type'] == 'basic'
>       assert session['auth']['username'] == 'username'
E       KeyError: 'username'

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_auth_0.py:10: KeyError
____________________________ test_missing_auth_type ____________________________

    def test_missing_auth_type():
        with pytest.raises(AssertionError):
            session = Session(path='fake_path')
            session['auth'] = {'raw_auth': 'username:password'}
    
>           assert session['auth']['type'] is None
E           KeyError: 'type'

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_auth_0.py:18: KeyError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_auth_0.py::test_valid_auth
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_auth_0.py::test_missing_auth_type
========================= 2 failed, 1 warning in 0.48s =========================
"""