
import pytest
from ansible.utils._collections_config import _AnsibleCollectionConfig

# Test initialization of _AnsibleCollectionConfig with metadata
def test_init_with_metadata():
    meta = {'name': 'test_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'test_collection')
    
    assert hasattr(config, '_collection_finder'), "Expected _collection_finder attribute to be set"
    assert config._default_collection is None, "_default_collection should be initialized to None"
    assert isinstance(config._on_collection_load, _EventSource), "_on_collection_load should be an instance of _EventSource"

# Test setting collection finder
def test_set_collection_finder():
    config = _AnsibleCollectionConfig({}, 'test_collection')
    from ansible.module_utils._collections_compat import _AnsibleCollectionFinder
    
    collection_finder = _AnsibleCollectionFinder()
    config._collection_finder = collection_finder
    
    assert isinstance(config._collection_finder, _AnsibleCollectionFinder), "_collection_finder should be an instance of _AnsibleCollectionFinder"

# Test setting default collection
def test_set_default_collection():
    config = _AnsibleCollectionConfig({}, 'test_collection')
    config._default_collection = 'default_collection'
    
    assert config._default_collection == 'default_collection', "_default_collection should be set to 'default_collection'"

# Test retrieving collection paths
def test_retrieve_collection_paths():
    config = _AnsibleCollectionConfig({}, 'test_collection')
    from ansible.module_utils._collections_compat import _AnsibleCollectionFinder
    
    collection_finder = _AnsibleCollectionFinder()
    collection_finder._n_collection_paths = ['path1', 'path2']
    config._collection_finder = collection_finder
    
    paths = config.collection_paths()
    assert isinstance(paths, list), "Expected a list of paths"
    assert len(paths) == 2, "Expected two paths in the list"
    assert all(isinstance(p, str) for p in paths), "All paths should be strings"

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
_ ERROR collecting test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_collection_paths_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_collection_paths_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_collection_paths_0.py:3: in <module>
    from ansible.utils._collections_config import _AnsibleCollectionConfig
E   ModuleNotFoundError: No module named 'ansible.utils._collections_config'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_collection_paths_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.78s ===============================
"""