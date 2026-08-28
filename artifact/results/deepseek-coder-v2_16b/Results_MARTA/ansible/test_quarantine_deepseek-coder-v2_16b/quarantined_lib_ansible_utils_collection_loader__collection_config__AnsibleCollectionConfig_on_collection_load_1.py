
import pytest
from ansible.utils._collections_config import _AnsibleCollectionConfig

# Test initialization of _AnsibleCollectionConfig without errors
def test_init_ansible_collection_config():
    meta = {'name': 'my_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'my_collection')
    
    assert hasattr(config, '_collection_finder'), "Expected _collection_finder to be set"
    assert hasattr(config, '_default_collection'), "Expected _default_collection to be set"
    assert isinstance(config._on_collection_load, _EventSource), "_on_collection_load should be an instance of _EventSource"

# Test setting on_collection_load with valid value
def test_set_valid_on_collection_load():
    meta = {'name': 'my_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'my_collection')
    
    new_event_source = _EventSource()
    config.on_collection_load(new_event_source)
    
    assert config._on_collection_load == new_event_source, "Expected on_collection_load to be set to the provided value"

# Test setting on_collection_load with invalid value raises ValueError
def test_set_invalid_on_collection_load():
    meta = {'name': 'my_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'my_collection')
    
    with pytest.raises(ValueError):
        config.on_collection_load(_EventSource())

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
_ ERROR collecting test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_on_collection_load_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_on_collection_load_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_on_collection_load_1.py:3: in <module>
    from ansible.utils._collections_config import _AnsibleCollectionConfig
E   ModuleNotFoundError: No module named 'ansible.utils._collections_config'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__AnsibleCollectionConfig_on_collection_load_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.78s ===============================
"""