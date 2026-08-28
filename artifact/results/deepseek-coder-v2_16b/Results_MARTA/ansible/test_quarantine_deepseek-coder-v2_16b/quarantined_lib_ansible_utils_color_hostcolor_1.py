
import pytest
from ansible.utils.color import hostcolor




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_hostcolor_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_________________________ test_hostcolor_with_changes __________________________

    def test_hostcolor_with_changes():
>       assert hostcolor("localhost", {"failures": 0, "unreachable": 0, "changed": 1}) == 'localhost'
E       AssertionError: assert 'localhost                 ' == 'localhost'
E         
E         - localhost
E         + localhost

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_hostcolor_1.py:6: AssertionError
_________________________ test_hostcolor_without_color _________________________

    def test_hostcolor_without_color():
>       assert hostcolor("anotherhost", {"failures": 0, "unreachable": 0, "changed": 0}, color=False) == 'anotherhost'
E       AssertionError: assert 'anotherhost               ' == 'anotherhost'
E         
E         - anotherhost
E         + anotherhost

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_hostcolor_1.py:9: AssertionError
__________________________ test_hostcolor_with_errors __________________________

    def test_hostcolor_with_errors():
>       assert hostcolor("remotehost", {"failures": 2, "unreachable": 1, "changed": 0}) == '\033[38;5;2mremotehost\033[0m'
E       AssertionError: assert 'remotehost                ' == '\x1b[38;5;2m...tehost\x1b[0m'
E         
E         - [38;5;2mremotehost[0m
E         + remotehost

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_hostcolor_1.py:12: AssertionError
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_hostcolor_1.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_hostcolor_1.py::test_hostcolor_with_changes
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_hostcolor_1.py::test_hostcolor_without_color
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_hostcolor_1.py::test_hostcolor_with_errors
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_hostcolor_1.py::test_invalid_input_error_handling
============================== 4 failed in 0.80s ===============================
"""