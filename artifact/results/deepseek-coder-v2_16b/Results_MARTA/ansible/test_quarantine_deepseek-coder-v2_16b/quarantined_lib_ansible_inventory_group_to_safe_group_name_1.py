
import pytest
from ansible.inventory.group import to_safe_group_name

# Test case for basic group name sanitization

# Test case for forcing replacement of invalid characters

# Test case for silencing warnings about replacements

# Test case for combining force and silent options
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________________ test_basic_sanitization ____________________________

    def test_basic_sanitization():
        result = to_safe_group_name("my-group_name")
>       assert result == "my_group_name"
E       AssertionError: assert 'my-group_name' == 'my_group_name'
E         
E         - my_group_name
E         ?   ^
E         + my-group_name
E         ?   ^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_1.py:8: AssertionError
----------------------------- Captured stderr call -----------------------------
[WARNING]: Invalid characters were found in group names but not replaced, use
-vvvv to see details
____________________________ test_force_replacement ____________________________

    def test_force_replacement():
        result = to_safe_group_name("my-group!name", force=True)
>       assert result == "my_group_name_"
E       AssertionError: assert 'my_group_name' == 'my_group_name_'
E         
E         - my_group_name_
E         ?              -
E         + my_group_name

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_1.py:13: AssertionError
----------------------------- Captured stderr call -----------------------------
[WARNING]: Invalid characters were found in group names and automatically
replaced, use -vvvv to see details
______________________________ test_silent_option ______________________________

    def test_silent_option():
        result = to_safe_group_name("my-group!name", silent=True)
>       assert result == "my_group_name_"
E       AssertionError: assert 'my-group!name' == 'my_group_name_'
E         
E         - my_group_name_
E         ?   ^     ^    -
E         + my-group!name
E         ?   ^     ^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_1.py:18: AssertionError
____________________________ test_combined_options _____________________________

    def test_combined_options():
        result = to_safe_group_name("my-group!name", force=True, silent=True)
>       assert result == "my_group_name_"
E       AssertionError: assert 'my_group_name' == 'my_group_name_'
E         
E         - my_group_name_
E         ?              -
E         + my_group_name

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_1.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_1.py::test_basic_sanitization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_1.py::test_force_replacement
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_1.py::test_silent_option
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_group_to_safe_group_name_1.py::test_combined_options
============================== 4 failed in 0.76s ===============================
"""