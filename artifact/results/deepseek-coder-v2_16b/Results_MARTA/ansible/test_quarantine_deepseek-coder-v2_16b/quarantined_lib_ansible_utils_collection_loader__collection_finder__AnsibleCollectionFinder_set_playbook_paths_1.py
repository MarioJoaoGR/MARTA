
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def valid_finder():
    return _AnsibleCollectionFinder(paths=['/path/to/collection1', '/path/to/collection2'], scan_sys_paths=True)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder_set_playbook_paths_1.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

valid_finder = <ansible.utils.collection_loader._collection_finder._AnsibleCollectionFinder object at 0x7f6edb07ebc0>

    def test_valid_input(valid_finder):
        assert isinstance(valid_finder, _AnsibleCollectionFinder), "The object is not an instance of _AnsibleCollectionFinder"
>       assert valid_finder._n_configured_paths == ['/path/to/collection1', '/path/to/collection2'], f"Expected paths to be {['/path/to/collection1', '/path/to/collection2']}, but got {valid_finder._n_configured_paths}"
E       AssertionError: Expected paths to be ['/path/to/collection1', '/path/to/collection2'], but got []
E       assert [] == ['/path/to/co.../collection2']
E         
E         Right contains 2 more items, first extra item: '/path/to/collection1'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder_set_playbook_paths_1.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionFinder_set_playbook_paths_1.py::test_valid_input
============================== 1 failed in 0.38s ===============================
"""