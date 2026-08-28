
import pytest
from thefuck.rules.sudo_command_from_user_path import get_new_command, _get_command_name


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_sudo_command_from_user_path_get_new_command_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        command = "sudo: unknownuser: command not found"
        expected_output = 'env "PATH=$PATH" unknownuser'
>       assert get_new_command(command) == expected_output

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_sudo_command_from_user_path_get_new_command_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/sudo_command_from_user_path.py:19: in get_new_command
    command_name = _get_command_name(command)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = 'sudo: unknownuser: command not found'

    def _get_command_name(command):
>       found = re.findall(r'sudo: (.*): command not found', command.output)
E       AttributeError: 'str' object has no attribute 'output'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/sudo_command_from_user_path.py:6: AttributeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        command = "This is a normal output without any error message."
>       assert get_new_command(command) is None

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_sudo_command_from_user_path_get_new_command_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/sudo_command_from_user_path.py:19: in get_new_command
    command_name = _get_command_name(command)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = 'This is a normal output without any error message.'

    def _get_command_name(command):
>       found = re.findall(r'sudo: (.*): command not found', command.output)
E       AttributeError: 'str' object has no attribute 'output'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/sudo_command_from_user_path.py:6: AttributeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_sudo_command_from_user_path_get_new_command_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_sudo_command_from_user_path_get_new_command_0.py::test_invalid_input
========================= 2 failed, 1 warning in 0.13s =========================
"""