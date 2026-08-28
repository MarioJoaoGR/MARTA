
import pytest
from ansible.playbook.base import FieldAttributeBase



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__extend_value_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_extend_value_with_none __________________________

    def test_extend_value_with_none():
        field = FieldAttributeBase()
        value = [None, 1]
        new_value = None
        extended_value = field._extend_value(value, new_value)
>       assert extended_value == [None, 1], f"Expected [None, 1], but got {extended_value}"
E       AssertionError: Expected [None, 1], but got [1]
E       assert [1] == [None, 1]
E         
E         At index 0 diff: 1 != None
E         Right contains one more item: 1
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__extend_value_1.py:10: AssertionError
_________________________ test_extend_value_with_list __________________________

    def test_extend_value_with_list():
        field = FieldAttributeBase()
        value = [1]
        new_value = [2, None]
        extended_value = field._extend_value(value, new_value)
>       assert extended_value == [1, 2, None], f"Expected [1, 2, None], but got {extended_value}"
E       AssertionError: Expected [1, 2, None], but got [1, 2]
E       assert [1, 2] == [1, 2, None]
E         
E         Right contains one more item: None
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__extend_value_1.py:17: AssertionError
________________________ test_extend_value_with_prepend ________________________

    def test_extend_value_with_prepend():
        field = FieldAttributeBase()
        value = [1]
        new_value = [None, 2]
        extended_value = field._extend_value(value, new_value, prepend=True)
>       assert extended_value == [None, 2, 1], f"Expected [None, 2, 1], but got {extended_value}"
E       AssertionError: Expected [None, 2, 1], but got [2, 1]
E       assert [2, 1] == [None, 2, 1]
E         
E         At index 0 diff: 2 != None
E         Right contains one more item: 1
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__extend_value_1.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__extend_value_1.py::test_extend_value_with_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__extend_value_1.py::test_extend_value_with_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__extend_value_1.py::test_extend_value_with_prepend
============================== 3 failed in 0.76s ===============================
"""