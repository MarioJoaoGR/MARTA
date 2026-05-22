
import pytest
from httpie.manager.tasks.sessions import cli_upgrade_session, upgrade_session, get_httpie_session
from httpie.sessions import Environment
from argparse import Namespace
from unittest.mock import patch

def test_invalid_inputs():
    env = Environment()
    args = Namespace(hostname=123, session='session123')
    
    with pytest.raises(TypeError):
        with patch('httpie.sessions.session_hostname_to_dirname', side_effect=AttributeError("'int' object has no attribute 'replace'")):
            cli_upgrade_session(env, args)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_sessions_cli_upgrade_session_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        env = Environment()
        args = Namespace(hostname=123, session='session123')
    
        with pytest.raises(TypeError):
            with patch('httpie.sessions.session_hostname_to_dirname', side_effect=AttributeError("'int' object has no attribute 'replace'")):
>               cli_upgrade_session(env, args)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_sessions_cli_upgrade_session_2_test_invalid_inputs.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/sessions.py:64: in cli_upgrade_session
    return upgrade_session(
httpie/httpie/manager/tasks/sessions.py:31: in upgrade_session
    session = get_httpie_session(
httpie/httpie/sessions.py:110: in get_httpie_session
    path = config_dir / session_hostname_to_dirname(bound_hostname, session_name)
/usr/local/lib/python3.11/unittest/mock.py:1124: in __call__
    return self._mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1128: in _mock_call
    return self._execute_mock_call(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='session_hostname_to_dirname' id='140248979532496'>
args = (123, 'session123'), kwargs = {}
effect = AttributeError("'int' object has no attribute 'replace'")

    def _execute_mock_call(self, /, *args, **kwargs):
        # separate from _increment_mock_call so that awaited functions are
        # executed separately from their call, also AsyncMock overrides this method
    
        effect = self.side_effect
        if effect is not None:
            if _is_exception(effect):
>               raise effect
E               AttributeError: 'int' object has no attribute 'replace'

/usr/local/lib/python3.11/unittest/mock.py:1183: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_sessions_cli_upgrade_session_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.32s ===============================
"""