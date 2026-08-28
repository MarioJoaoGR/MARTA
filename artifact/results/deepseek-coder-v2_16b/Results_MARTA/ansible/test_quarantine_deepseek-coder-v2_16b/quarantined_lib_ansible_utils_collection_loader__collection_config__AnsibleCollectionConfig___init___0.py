
import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_init_without_paths ____________________________

    def test_init_without_paths():
        class MetaClass: pass
>       config = _AnsibleCollectionConfig(MetaClass, "TestClass", (object,))
E       TypeError: type.__new__() argument 1 must be str, not type

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig___init___0.py:7: TypeError
_____________________________ test_init_with_paths _____________________________

    def test_init_with_paths():
        class MetaClass: pass
>       config = _AnsibleCollectionConfig(MetaClass, "TestClass", (object,), paths=['/custom/collection/path'])
E       TypeError: type.__new__() argument 1 must be str, not type

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig___init___0.py:17: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig___init___0.py::test_init_without_paths
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig___init___0.py::test_init_with_paths
============================== 2 failed in 0.49s ===============================
"""