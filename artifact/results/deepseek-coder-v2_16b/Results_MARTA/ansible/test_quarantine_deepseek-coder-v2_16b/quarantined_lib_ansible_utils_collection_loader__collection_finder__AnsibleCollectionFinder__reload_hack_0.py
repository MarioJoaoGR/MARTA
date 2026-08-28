
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder__reload_hack_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________________ test_valid_initialization ___________________________

    def test_valid_initialization():
        finder = _AnsibleCollectionFinder(paths=['/path/to/collection1', '/path/to/collection2'], scan_sys_paths=True)
>       assert finder._n_configured_paths == ['/path/to/collection1', '/path/to/collection2']
E       AssertionError: assert [] == ['/path/to/co.../collection2']
E         
E         Right contains 2 more items, first extra item: '/path/to/collection1'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder__reload_hack_0.py:9: AssertionError
____________________ test_single_string_path_initialization ____________________

    def test_single_string_path_initialization():
        finder = _AnsibleCollectionFinder(paths='/path/to/collection')
>       assert finder._n_configured_paths == ['/path/to/collection']
E       AssertionError: assert [] == ['/path/to/collection']
E         
E         Right contains one more item: '/path/to/collection'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder__reload_hack_0.py:13: AssertionError
____________________________ test_configured_paths _____________________________

    def test_configured_paths():
        finder = _AnsibleCollectionFinder(paths=['/path/to/collection1', '/path/to/collection2'], scan_sys_paths=True)
>       assert finder._n_configured_paths == ['/path/to/collection1', '/path/to/collection2']
E       AssertionError: assert [] == ['/path/to/co.../collection2']
E         
E         Right contains 2 more items, first extra item: '/path/to/collection1'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder__reload_hack_0.py:17: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder__reload_hack_0.py:20: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder__reload_hack_0.py::test_valid_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder__reload_hack_0.py::test_single_string_path_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder__reload_hack_0.py::test_configured_paths
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder__reload_hack_0.py::test_invalid_input
============================== 4 failed in 0.39s ===============================
"""