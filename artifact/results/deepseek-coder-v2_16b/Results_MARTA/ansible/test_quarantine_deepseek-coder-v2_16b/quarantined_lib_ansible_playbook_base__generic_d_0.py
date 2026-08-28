
import pytest
from ansible.playbook.base import ExampleClass

def test_generic_d_existing_property():
    class TestObject:
        def __init__(self):
            self._attributes = {'property1': 'value1', 'property2': 'value2'}
        
        def _generic_d(self, prop_name):
            del self._attributes[prop_name]
    
    test_obj = TestObject()
    assert len(test_obj._attributes) == 2
    test_obj._generic_d('property1')
    assert 'property1' not in test_obj._attributes
    assert len(test_obj._attributes) == 1

def test_generic_d_nonexistent_property():
    class TestObject:
        def __init__(self):
            self._attributes = {'property1': 'value1'}
        
        def _generic_d(self, prop_name):
            del self._attributes[prop_name]
    
    test_obj = TestObject()
    with pytest.raises(KeyError):
        test_obj._generic_d('property2')
    assert 'property1' in test_obj._attributes

def test_generic_d_empty_object():
    class TestObject:
        def __init__(self):
            self._attributes = {}
        
        def _generic_d(self, prop_name):
            del self._attributes[prop_name]
    
    test_obj = TestObject()
    with pytest.raises(KeyError):
        test_obj._generic_d('property1')
    assert len(test_obj._attributes) == 0

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
_______ ERROR collecting test_lib_ansible_playbook_base__generic_d_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base__generic_d_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base__generic_d_0.py:3: in <module>
    from ansible.playbook.base import ExampleClass
E   ImportError: cannot import name 'ExampleClass' from 'ansible.playbook.base' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/base.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base__generic_d_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.53s ===============================
"""