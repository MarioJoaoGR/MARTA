
import pytest
import argparse
from ansible.cli.arguments.option_helpers import add_runas_options



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_2.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_add_runas_options_default ________________________

    def test_add_runas_options_default():
        parser = argparse.ArgumentParser()
        add_runas_options(parser)
    
        args = parser.parse_args([])
    
        assert not args.become, "Expected become to be False by default"
>       assert args.become_method is None, "Expected become_method to be None by default"
E       AssertionError: Expected become_method to be None by default
E       assert 'sudo' is None
E        +  where 'sudo' = Namespace(become=False, become_method='sudo', become_user=None, become_ask_pass=False, become_password_file=None).become_method

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_2.py:13: AssertionError
______________________ test_add_runas_options_with_become ______________________

    def test_add_runas_options_with_become():
        parser = argparse.ArgumentParser()
        add_runas_options(parser)
    
        args = parser.parse_args(['--become'])
    
        assert args.become, "Expected become to be True when passed"
>       assert args.become_method is None, "Expected become_method to remain None even when --become is used"
E       AssertionError: Expected become_method to remain None even when --become is used
E       assert 'sudo' is None
E        +  where 'sudo' = Namespace(become=True, become_method='sudo', become_user=None, become_ask_pass=False, become_password_file=None).become_method

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_2.py:22: AssertionError
___________________ test_add_runas_options_with_become_user ____________________

    def test_add_runas_options_with_become_user():
        parser = argparse.ArgumentParser()
        add_runas_options(parser)
    
        args = parser.parse_args(['--become-user', 'root'])
    
        assert not args.become, "Expected become to be False when only --become-user is used"
>       assert args.become_method is None, "Expected become_method to remain None even when --become-user is used"
E       AssertionError: Expected become_method to remain None even when --become-user is used
E       assert 'sudo' is None
E        +  where 'sudo' = Namespace(become=False, become_method='sudo', become_user='root', become_ask_pass=False, become_password_file=None).become_method

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_2.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_2.py::test_add_runas_options_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_2.py::test_add_runas_options_with_become
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runas_options_2.py::test_add_runas_options_with_become_user
============================== 3 failed in 1.00s ===============================
"""