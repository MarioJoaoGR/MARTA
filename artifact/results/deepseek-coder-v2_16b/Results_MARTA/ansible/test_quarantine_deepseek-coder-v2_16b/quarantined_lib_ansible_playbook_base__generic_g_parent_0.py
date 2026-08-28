
import pytest
from ansible.playbook.base import BaseClass

def test_generic_g_parent_retrieves_property_from_self():
    class MyClass(BaseClass):
        def __init__(self):
            self.name = "Example Name"
            self._attributes = {'name': 'Example Name'}
    
    my_instance = MyClass()
    prop_value = _generic_g_parent('name', my_instance)
    assert prop_value == 'Example Name'

def test_generic_g_parent_retrieves_property_from_parent():
    class ParentClass:
        def __init__(self):
            self.age = 30
    
    class MyClass(ParentClass, BaseClass):
        def __init__(self):
            super().__init__()
            self._attributes = {'name': 'Example Name'}
    
    my_instance = MyClass()
    prop_value = _generic_g_parent('age', my_instance)
    assert prop_value == 30

def test_generic_g_parent_raises_attribute_error():
    class MyClass(BaseClass):
        def __init__(self):
            self._attributes = {'name': 'Example Name'}
    
    my_instance = MyClass()
    with pytest.raises(AttributeError) as e:
        _generic_g_parent('non_existent_property', my_instance)
    assert str(e.value) == "'MyClass' object has no attribute 'non_existent_property'"

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
____ ERROR collecting test_lib_ansible_playbook_base__generic_g_parent_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base__generic_g_parent_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base__generic_g_parent_0.py:3: in <module>
    from ansible.playbook.base import BaseClass
E   ImportError: cannot import name 'BaseClass' from 'ansible.playbook.base' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/base.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base__generic_g_parent_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.54s ===============================
"""