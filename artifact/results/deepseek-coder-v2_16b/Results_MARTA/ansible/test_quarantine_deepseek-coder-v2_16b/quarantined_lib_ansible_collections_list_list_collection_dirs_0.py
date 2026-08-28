
import pytest
from ansible.collections.list import list_collection_dirs
import os




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_collections_list_list_collection_dirs_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________________ test_default_configuration __________________________

    def test_default_configuration():
        collections = list_collection_dirs()
>       assert isinstance(collections, list), f"Expected a list of paths but got {type(collections)} for default configuration"
E       AssertionError: Expected a list of paths but got <class 'generator'> for default configuration
E       assert False
E        +  where False = isinstance(<generator object list_collection_dirs at 0x7f38ff9ac970>, list)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_collections_list_list_collection_dirs_0.py:8: AssertionError
__________________ test_specific_namespace_without_collection __________________

    def test_specific_namespace_without_collection():
        specific_namespace_collections = list_collection_dirs(coll_filter="my_namespace")
>       assert isinstance(specific_namespace_collections, list), f"Expected a list of paths but got {type(specific_namespace_collections)} for specific namespace without collection"
E       AssertionError: Expected a list of paths but got <class 'generator'> for specific namespace without collection
E       assert False
E        +  where False = isinstance(<generator object list_collection_dirs at 0x7f38ff851a80>, list)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_collections_list_list_collection_dirs_0.py:12: AssertionError
____________________ test_specific_namespace_and_collection ____________________

    def test_specific_namespace_and_collection():
        specific_collections = list_collection_dirs(coll_filter="my_namespace.specific_collection")
>       assert isinstance(specific_collections, list), f"Expected a list of paths but got {type(specific_collections)} for specific namespace and collection"
E       AssertionError: Expected a list of paths but got <class 'generator'> for specific namespace and collection
E       assert False
E        +  where False = isinstance(<generator object list_collection_dirs at 0x7f38ff8520a0>, list)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_collections_list_list_collection_dirs_0.py:16: AssertionError
___________________________ test_custom_search_paths ___________________________

    def test_custom_search_paths():
        custom_search_paths = ['path1', 'path2']
        specific_collections = list_collection_dirs(search_paths=custom_search_paths, coll_filter="my_namespace.specific_collection")
>       assert isinstance(specific_collections, list), f"Expected a list of paths but got {type(specific_collections)} for custom search paths and specific namespace and collection"
E       AssertionError: Expected a list of paths but got <class 'generator'> for custom search paths and specific namespace and collection
E       assert False
E        +  where False = isinstance(<generator object list_collection_dirs at 0x7f38ff8526c0>, list)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_collections_list_list_collection_dirs_0.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_collections_list_list_collection_dirs_0.py::test_default_configuration
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_collections_list_list_collection_dirs_0.py::test_specific_namespace_without_collection
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_collections_list_list_collection_dirs_0.py::test_specific_namespace_and_collection
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_collections_list_list_collection_dirs_0.py::test_custom_search_paths
============================== 4 failed in 0.65s ===============================
"""