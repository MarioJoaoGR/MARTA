
import pytest
import os
from ansible.plugins.callback import junit

@pytest.fixture(scope="module")
def setup_valid_inputs():
    # Set up environment variables for valid inputs
    os.environ['JUNIT_OUTPUT_DIR'] = '~/.ansible/junit'
    os.environ['JUNIT_TASK_CLASS'] = 'True'
    os.environ['JUNIT_TASK_RELATIVE_PATH'] = 'relative'
    os.environ['JUNIT_FAIL_ON_CHANGE'] = 'True'
    os.environ['JUNIT_FAIL_ON_IGNORE'] = 'True'
    os.environ['JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT'] = 'False'
    os.environ['JUNIT_HIDE_TASK_ARGUMENTS'] = 'True'
    os.environ['JUNIT_TEST_CASE_PREFIX'] = 'test_'
    
    callback = junit.CallbackModule()
    yield callback
    # Teardown: Remove environment variables if necessary
    del os.environ['JUNIT_OUTPUT_DIR']
    del os.environ['JUNIT_TASK_CLASS']
    del os.environ['JUNIT_TASK_RELATIVE_PATH']
    del os.environ['JUNIT_FAIL_ON_CHANGE']
    del os.environ['JUNIT_FAIL_ON_IGNORE']
    del os.environ['JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT']
    del os.environ['JUNIT_HIDE_TASK_ARGUMENTS']
    del os.environ['JUNIT_TEST_CASE_PREFIX']


@pytest.fixture(scope="module")
def setup_invalid_inputs():
    # Set up environment variables for invalid inputs
    os.environ['JUNIT_OUTPUT_DIR'] = 'invalid_dir'  # Invalid directory to trigger an error
    os.environ['JUNIT_TASK_CLASS'] = 'True'
    os.environ['JUNIT_TASK_RELATIVE_PATH'] = 'relative'
    os.environ['JUNIT_FAIL_ON_CHANGE'] = 'True'
    os.environ['JUNIT_FAIL_ON_IGNORE'] = 'True'
    os.environ['JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT'] = 'False'
    os.environ['JUNIT_HIDE_TASK_ARGUMENTS'] = 'True'
    os.environ['JUNIT_TEST_CASE_PREFIX'] = 'test_'
    
    callback = junit.CallbackModule()
    yield callback
    # Teardown: Remove environment variables if necessary
    del os.environ['JUNIT_OUTPUT_DIR']
    del os.environ['JUNIT_TASK_CLASS']
    del os.environ['JUNIT_TASK_RELATIVE_PATH']
    del os.environ['JUNIT_FAIL_ON_CHANGE']
    del os.environ['JUNIT_FAIL_ON_IGNORE']
    del os.environ['JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT']
    del os.environ['JUNIT_HIDE_TASK_ARGUMENTS']
    del os.environ['JUNIT_TEST_CASE_PREFIX']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_CallbackModule_v2_playbook_on_task_start_0.py F [ 50%]
.E                                                                       [100%]

==================================== ERRORS ====================================
___________________ ERROR at teardown of test_invalid_inputs ___________________

    @pytest.fixture(scope="module")
    def setup_valid_inputs():
        # Set up environment variables for valid inputs
        os.environ['JUNIT_OUTPUT_DIR'] = '~/.ansible/junit'
        os.environ['JUNIT_TASK_CLASS'] = 'True'
        os.environ['JUNIT_TASK_RELATIVE_PATH'] = 'relative'
        os.environ['JUNIT_FAIL_ON_CHANGE'] = 'True'
        os.environ['JUNIT_FAIL_ON_IGNORE'] = 'True'
        os.environ['JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT'] = 'False'
        os.environ['JUNIT_HIDE_TASK_ARGUMENTS'] = 'True'
        os.environ['JUNIT_TEST_CASE_PREFIX'] = 'test_'
    
        callback = junit.CallbackModule()
        yield callback
        # Teardown: Remove environment variables if necessary
>       del os.environ['JUNIT_OUTPUT_DIR']

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_CallbackModule_v2_playbook_on_task_start_0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '...est_lib_ansible_plugins_callback_junit_CallbackModule_v2_playbook_on_task_start_0.py::test_invalid_inputs (teardown)'})
key = 'JUNIT_OUTPUT_DIR'

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
>           raise KeyError(key) from None
E           KeyError: 'JUNIT_OUTPUT_DIR'

/opt/conda/envs/test4py_env/lib/python3.10/os.py:696: KeyError
=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

setup_valid_inputs = <ansible.plugins.callback.junit.CallbackModule object at 0x7eff7c0f35b0>

    def test_valid_inputs(setup_valid_inputs):
        callback = setup_valid_inputs
        assert isinstance(callback, junit.CallbackModule)
>       assert callback._output_dir == os.path.expanduser('~/.ansible/junit')
E       AssertionError: assert '~/.ansible/junit' == '/home/joaovi...ansible/junit'
E         
E         - /home/joaovitorino/.ansible/junit
E         + ~/.ansible/junit

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_CallbackModule_v2_playbook_on_task_start_0.py:33: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_CallbackModule_v2_playbook_on_task_start_0.py::test_valid_inputs
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_CallbackModule_v2_playbook_on_task_start_0.py::test_invalid_inputs
===================== 1 failed, 1 passed, 1 error in 0.55s =====================
"""