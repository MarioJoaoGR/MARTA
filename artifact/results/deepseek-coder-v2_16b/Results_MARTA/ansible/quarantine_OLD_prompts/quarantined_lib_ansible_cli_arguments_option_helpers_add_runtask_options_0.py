
import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_runtask_options, maybe_unfrack_path



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runtask_options_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________ test_add_runtask_options_inline_key_value ___________________

    def test_add_runtask_options_inline_key_value():
        parser = ArgumentParser()
>       with pytest.raises(SystemExit):
E       Failed: DID NOT RAISE <class 'SystemExit'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runtask_options_0.py:8: Failed
___________________ test_add_runtask_options_file_reference ____________________

    def test_add_runtask_options_file_reference():
        parser = ArgumentParser()
>       with pytest.raises(SystemExit):
E       Failed: DID NOT RAISE <class 'SystemExit'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runtask_options_0.py:15: Failed
______________ test_add_runtask_options_multiple_inline_and_file _______________

    def test_add_runtask_options_multiple_inline_and_file():
        parser = ArgumentParser()
>       with pytest.raises(SystemExit):
E       Failed: DID NOT RAISE <class 'SystemExit'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runtask_options_0.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runtask_options_0.py::test_add_runtask_options_inline_key_value
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runtask_options_0.py::test_add_runtask_options_file_reference
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_runtask_options_0.py::test_add_runtask_options_multiple_inline_and_file
============================== 3 failed in 0.60s ===============================
"""