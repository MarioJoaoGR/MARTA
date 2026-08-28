
import pytest
from ansible.plugins.callback import default

@pytest.fixture(autouse=True)
def callback_module():
    return default.CallbackModule()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_runner_on_async_failed_1.py F [100%]

=================================== FAILURES ===================================
________________________ test_v2_runner_on_async_failed ________________________

callback_module = <ansible.plugins.callback.default.CallbackModule object at 0x7f57093fd1e0>

    def test_v2_runner_on_async_failed(callback_module):
        class MockResult:
            def __init__(self, host):
                self._host = host
                self._result = {'ansible_job_id': '12345'}
    
>       mock_host = MockHost()
E       NameError: name 'MockHost' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_runner_on_async_failed_1.py:15: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_runner_on_async_failed_1.py::test_v2_runner_on_async_failed
============================== 1 failed in 0.83s ===============================
"""