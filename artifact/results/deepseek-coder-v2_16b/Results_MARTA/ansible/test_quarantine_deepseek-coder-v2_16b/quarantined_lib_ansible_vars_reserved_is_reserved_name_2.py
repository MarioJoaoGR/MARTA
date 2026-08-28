
import pytest
from ansible.vars.reserved import _RESERVED_NAMES

def is_reserved_name(name):
    return name in _RESERVED_NAMES

# Test for valid input - happy path

# Test for invalid input - None type
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_is_reserved_name_2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
>       assert is_reserved_name("if") == True
E       AssertionError: assert False == True
E        +  where False = is_reserved_name('if')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_is_reserved_name_2.py:10: AssertionError
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_is_reserved_name_2.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_is_reserved_name_2.py::test_valid_input_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_is_reserved_name_2.py::test_invalid_input_none
============================== 2 failed in 0.97s ===============================
"""