
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionPkgLoader
import os
import importlib

@pytest.fixture(scope="module")
def collection_loader():
    return AnsibleCollectionPkgLoader()

def test_load_ansible_builtin_module(collection_loader):
    module = collection_loader.load_module('ansible.builtin')
    assert hasattr(module, '_collection_meta'), "Module should have _collection_meta attribute"
    assert isinstance(module._collection_meta, dict), "_collection_meta should be a dictionary"
    print(module._collection_meta)  # Output will show metadata for the 'ansible.builtin' collection

def test_load_custom_module(collection_loader):
    module = collection_loader.load_module('mynamespace.mycollection.mymodule')
    assert hasattr(module, '_collection_meta'), "Module should have _collection_meta attribute"
    assert isinstance(module._collection_meta, dict), "_collection_meta should be a dictionary"
    print(module._collection_meta)  # Output will show metadata for the custom collection

def test_load_module_from_specific_path(collection_loader):
    local_ansible_path = os.path.dirname(importlib.__file__)
    module = collection_loader.load_module('ansible.builtin', path_list=[local_ansible_path])
    assert hasattr(module, '_collection_meta'), "Module should have _collection_meta attribute"
    assert isinstance(module._collection_meta, dict), "_collection_meta should be a dictionary"
    print(module._collection_meta)  # Output will show metadata for the 'ansible.builtin' collection loaded from specific path

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionPkgLoader_load_module_2.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionPkgLoader_load_module_2.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionPkgLoader_load_module_2.py:3: in <module>
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionPkgLoader
E   ImportError: cannot import name 'AnsibleCollectionPkgLoader' from 'ansible.utils.collection_loader._collection_finder' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/collection_loader/_collection_finder.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__AnsibleCollectionPkgLoader_load_module_2.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.78s ===============================
"""