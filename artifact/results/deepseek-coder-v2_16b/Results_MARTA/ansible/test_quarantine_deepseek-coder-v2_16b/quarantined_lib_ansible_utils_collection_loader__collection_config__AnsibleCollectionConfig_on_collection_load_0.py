
import pytest
from ansible.utils._collections_config import _AnsibleCollectionConfig

# Test initialization of _AnsibleCollectionConfig without errors
def test_init_ansible_collection_config():
    meta = {'name': 'my_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'my_collection')
    
    assert hasattr(config, '_collection_finder'), "Expected _collection_finder attribute to be set"
    assert hasattr(config, '_default_collection'), "Expected _default_collection attribute to be set"
    assert hasattr(config, '_on_collection_load'), "Expected _on_collection_load attribute to be set"

# Test setting up collection finder correctly
def test_setup_collection_finder():
    meta = {'name': 'my_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'my_collection')
    
    def mock_finder(x): return x
    config.collection_finder(mock_finder)
    
    assert config._collection_finder == mock_finder, "Expected collection finder to be set correctly"

# Test setting default collection correctly
def test_set_default_collection():
    meta = {'name': 'my_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'my_collection')
    
    config.default_collection('my_default_collection')
    
    assert config._default_collection == 'my_default_collection', "Expected default collection to be set correctly"

# Test raising ValueError when trying to directly set on_collection_load
def test_raise_value_error_on_direct_set():
    meta = {'name': 'my_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'my_collection')
    
    with pytest.raises(ValueError) as excinfo:
        config.on_collection_load('some_value')
        
    assert str(excinfo.value) == "on_collection_load is not directly settable (use +=)", "Expected ValueError to be raised"

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
_ ERROR collecting test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_on_collection_load_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_on_collection_load_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_on_collection_load_0.py:3: in <module>
    from ansible.utils._collections_config import _AnsibleCollectionConfig
E   ModuleNotFoundError: No module named 'ansible.utils._collections_config'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_on_collection_load_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.41s ===============================
"""