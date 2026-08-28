
import pytest
from your_module import InventoryData

# Test adding a group to the inventory
def test_add_group():
    inventory = InventoryData()
    group_name = inventory.add_group('webservers')
    assert group_name == 'webservers'
    assert 'webservers' in inventory.groups

# Test adding a host to an existing group
def test_add_child_host():
    inventory = InventoryData()
    inventory.add_group('webservers')  # Ensure the group exists
    success = inventory.add_child('webservers', 'host1')
    assert success is True
    assert 'host1' in inventory.hosts
    assert 'webservers' in inventory.groups['webservers'].children

# Test adding a sub-group to an existing group
def test_add_child_subgroup():
    inventory = InventoryData()
    inventory.add_group('parent_group')  # Ensure the parent group exists
    success = inventory.add_child('parent_group', 'sub_group')
    assert success is True
    assert 'sub_group' in inventory.groups
    assert 'parent_group' in inventory.groups['sub_group'].parents

# Test adding a host to a non-existing group should raise an error
def test_add_child_non_existing_group():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        inventory.add_child('nonexistent_group', 'host1')

# Test adding a sub-group to a non-existing group should raise an error
def test_add_child_non_existing_subgroup():
    inventory = InventoryData()
    with pytest.raises(AnsibleError):
        inventory.add_child('parent_group', 'nonexistent_subgroup')

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
_ ERROR collecting test_lib_ansible_inventory_data_InventoryData_add_child_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_child_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_child_1.py:3: in <module>
    from your_module import InventoryData
E   ModuleNotFoundError: No module named 'your_module'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_child_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.40s ===============================
"""