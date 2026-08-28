
import pytest
from ansible.inventory.data import InventoryData, Host
from ansible.errors import AnsibleError




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_2.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_________________________ test_add_host_without_group __________________________

    def test_add_host_without_group():
        inventory = InventoryData()
        added_host = inventory.add_host('web1')
        assert added_host == 'web1'
        assert 'web1' in inventory.hosts
        assert inventory.hosts['web1'].name == 'web1'
        assert 'ungrouped' in inventory.groups
>       assert inventory.hosts['web1'] in inventory.groups['ungrouped'].hosts
E       assert web1 in []
E        +  where [] = ungrouped.hosts

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_2.py:13: AssertionError
_______________________ test_add_host_to_existing_group ________________________

    def test_add_host_to_existing_group():
        inventory = InventoryData()
        inventory.add_group('webservers')
        added_host = inventory.add_host('web1', 'webservers')
        assert added_host == 'web1'
        assert 'web1' in inventory.hosts
        assert inventory.hosts['web1'].name == 'web1'
        assert 'webservers' in inventory.groups
        assert inventory.hosts['web1'] in inventory.groups['webservers'].hosts
>       assert inventory.hosts['web1'].group_names == ['webservers']
E       AttributeError: 'Host' object has no attribute 'group_names'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_2.py:24: AttributeError
_______________________ test_add_host_with_specific_port _______________________

    def test_add_host_with_specific_port():
        inventory = InventoryData()
        inventory.add_group('webservers')
        added_host = inventory.add_host('web1', 'webservers', port=80)
        assert added_host == 'web1'
        assert 'web1' in inventory.hosts
        assert inventory.hosts['web1'].name == 'web1'
>       assert inventory.hosts['web1'].port == 80
E       AttributeError: 'Host' object has no attribute 'port'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_2.py:33: AttributeError
________________________ test_add_host_to_default_group ________________________

    def test_add_host_to_default_group():
        inventory = InventoryData()
        added_host = inventory.add_host('web1')
        assert added_host == 'web1'
        assert 'web1' in inventory.hosts
        assert inventory.hosts['web1'].name == 'web1'
        assert 'ungrouped' in inventory.groups
>       assert inventory.hosts['web1'] in inventory.groups['ungrouped'].hosts
E       assert web1 in []
E        +  where [] = ungrouped.hosts

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_2.py:42: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_2.py::test_add_host_without_group
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_2.py::test_add_host_to_existing_group
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_2.py::test_add_host_with_specific_port
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_2.py::test_add_host_to_default_group
============================== 4 failed in 0.85s ===============================
"""