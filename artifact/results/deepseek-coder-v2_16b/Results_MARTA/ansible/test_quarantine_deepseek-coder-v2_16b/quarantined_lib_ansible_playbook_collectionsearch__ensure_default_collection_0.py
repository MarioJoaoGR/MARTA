
import pytest
from ansible.playbook.collectionsearch import _ensure_default_collection




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________________ test_valid_input_no_params __________________________

    def test_valid_input_no_params():
        collection_list = None
        result = _ensure_default_collection(collection_list)
>       assert result == ['ansible.builtin', 'ansible.legacy']
E       AssertionError: assert [] == ['ansible.bui...sible.legacy']
E         
E         Right contains 2 more items, first extra item: 'ansible.builtin'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:8: AssertionError
_________________________ test_valid_input_empty_list __________________________

    def test_valid_input_empty_list():
        collection_list = []
        result = _ensure_default_collection(collection_list)
>       assert result == ['ansible.builtin', 'ansible.legacy']
E       AssertionError: assert [] == ['ansible.bui...sible.legacy']
E         
E         Right contains 2 more items, first extra item: 'ansible.builtin'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:13: AssertionError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        collection_list = None
        result = _ensure_default_collection(collection_list)
>       assert result == ['ansible.builtin', 'ansible.legacy']
E       AssertionError: assert [] == ['ansible.bui...sible.legacy']
E         
E         Right contains 2 more items, first extra item: 'ansible.builtin'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:18: AssertionError
__________________________ test_edge_case_empty_list ___________________________

    def test_edge_case_empty_list():
        collection_list = []
        result = _ensure_default_collection(collection_list)
>       assert result == ['ansible.builtin', 'ansible.legacy']
E       AssertionError: assert [] == ['ansible.bui...sible.legacy']
E         
E         Right contains 2 more items, first extra item: 'ansible.builtin'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_valid_input_no_params
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_valid_input_empty_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_edge_case_empty_list
============================== 4 failed in 0.49s ===============================
"""