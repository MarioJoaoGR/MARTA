
import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_tasknoplay_options
import constants as C  # Assuming constants are defined in a module named constants

def test_add_tasknoplay_options_default():
    parser = ArgumentParser()
    add_tasknoplay_options(parser)
    
    args = parser.parse_args([])
    assert hasattr(args, 'task_timeout')
    assert isinstance(args.task_timeout, int)
    assert args.task_timeout == C.TASK_TIMEOUT  # Default value should be 300 as per the function definition

def test_add_tasknoplay_options_custom():
    parser = ArgumentParser()
    add_tasknoplay_options(parser)
    
    args = parser.parse_args(['--task-timeout', '450'])
    assert hasattr(args, 'task_timeout')
    assert isinstance(args.task_timeout, int)
    assert args.task_timeout == 450

def test_add_tasknoplay_options_negative():
    parser = ArgumentParser()
    add_tasknoplay_options(parser)
    
    with pytest.raises(SystemExit):
        parser.parse_args(['--task-timeout', '-1'])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_cli_arguments_option_helpers_add_tasknoplay_options_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_tasknoplay_options_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_tasknoplay_options_0.py:5: in <module>
    import constants as C  # Assuming constants are defined in a module named constants
E   ModuleNotFoundError: No module named 'constants'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_tasknoplay_options_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.71s ===============================
"""