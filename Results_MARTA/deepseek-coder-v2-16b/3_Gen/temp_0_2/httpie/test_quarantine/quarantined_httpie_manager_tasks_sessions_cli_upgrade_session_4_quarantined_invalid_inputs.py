
import pytest
from httpie.manager.tasks.sessions import cli_upgrade_session, upgrade_session
from httpie.sessions import Environment
from argparse import Namespace
from httpie.manager.tasks.sessions import ExitStatus

def test_invalid_inputs():
    env = Environment()
    args = Namespace(hostname=123, session='session123')
    
    with pytest.raises(TypeError):
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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_sessions_cli_upgrade_session_4_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        env = Environment()
        args = Namespace(hostname=123, session='session123')
    
        with pytest.raises(TypeError):
>           cli_upgrade_session(env, args)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_sessions_cli_upgrade_session_4_test_invalid_inputs.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/sessions.py:64: in cli_upgrade_session
    return upgrade_session(
httpie/httpie/manager/tasks/sessions.py:31: in upgrade_session
    session = get_httpie_session(
httpie/httpie/sessions.py:110: in get_httpie_session
    path = config_dir / session_hostname_to_dirname(bound_hostname, session_name)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hostname = 123, session_name = 'session123'

    def session_hostname_to_dirname(hostname: str, session_name: str) -> str:
        # host:port => host_port
>       hostname = hostname.replace(':', '_')
E       AttributeError: 'int' object has no attribute 'replace'

httpie/httpie/sessions.py:48: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_tasks_sessions_cli_upgrade_session_4_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.31s ===============================
"""