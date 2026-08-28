
import pytest
from ansible.cli.adhoc import AdHocCLI



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_adhoc_AdHocCLI_post_process_args_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_minimal_options _______________________

    def test_valid_input_minimal_options():
>       cli = AdHocCLI()
E       TypeError: CLI.__init__() missing 1 required positional argument: 'args'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_adhoc_AdHocCLI_post_process_args_0.py:6: TypeError
________________________ test_valid_input_full_options _________________________

    def test_valid_input_full_options():
>       cli = AdHocCLI()
E       TypeError: CLI.__init__() missing 1 required positional argument: 'args'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_adhoc_AdHocCLI_post_process_args_0.py:16: TypeError
______________________ test_valid_input_custom_verbosity _______________________

    def test_valid_input_custom_verbosity():
>       cli = AdHocCLI()
E       TypeError: CLI.__init__() missing 1 required positional argument: 'args'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_adhoc_AdHocCLI_post_process_args_0.py:29: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_adhoc_AdHocCLI_post_process_args_0.py::test_valid_input_minimal_options
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_adhoc_AdHocCLI_post_process_args_0.py::test_valid_input_full_options
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_adhoc_AdHocCLI_post_process_args_0.py::test_valid_input_custom_verbosity
============================== 3 failed in 0.66s ===============================
"""