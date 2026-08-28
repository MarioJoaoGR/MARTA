
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionPkgLoader__validate_final_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_valid_input_builtin_namespace ______________________

    def test_valid_input_builtin_namespace():
>       loader = _AnsibleCollectionPkgLoader(split_name=['ansible', 'builtin'], subpackage_search_paths=['/path/to/collection'])
E       TypeError: _AnsibleCollectionPkgLoaderBase.__init__() got an unexpected keyword argument 'split_name'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionPkgLoader__validate_final_1.py:6: TypeError
_________________________ test_missing_candidate_path __________________________

    def test_missing_candidate_path():
        with pytest.raises(ImportError) as excinfo:
>           _AnsibleCollectionPkgLoader(split_name=['ansible', 'someothernamespace'], subpackage_search_paths=[])
E           TypeError: _AnsibleCollectionPkgLoaderBase.__init__() got an unexpected keyword argument 'split_name'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionPkgLoader__validate_final_1.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionPkgLoader__validate_final_1.py::test_valid_input_builtin_namespace
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionPkgLoader__validate_final_1.py::test_missing_candidate_path
============================== 2 failed in 0.72s ===============================
"""