
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder_find_module_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        finder = _AnsibleCollectionFinder(paths=['/path/to/collection1', '/path/to/collection2'], scan_sys_paths=True)
        assert isinstance(finder._n_configured_paths, list), "Expected configured paths to be a list"
>       assert len(finder._n_configured_paths) == 2, "Expected exactly two configured paths"
E       AssertionError: Expected exactly two configured paths
E       assert 0 == 2
E        +  where 0 = len([])
E        +    where [] = <ansible.utils.collection_loader._collection_finder._AnsibleCollectionFinder object at 0x7f0acc0b7970>._n_configured_paths

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder_find_module_1.py:8: AssertionError
_______________________________ test_error_case ________________________________

    def test_error_case():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder_find_module_1.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder_find_module_1.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder_find_module_1.py::test_error_case
============================== 2 failed in 0.76s ===============================
"""