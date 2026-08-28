
import pytest
from ansible.inventory.data import InventoryData, Host




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_________________________ test_add_host_without_group __________________________

    def test_add_host_without_group():
        inventory = InventoryData()
        added_host = inventory.add_host('web1')
        assert added_host == 'web1'
        assert 'web1' in inventory.hosts
        assert 'ungrouped' in inventory.groups
        assert inventory.hosts['web1'].name == 'web1'
>       assert inventory.hosts['web1'].port is None
E       AttributeError: 'Host' object has no attribute 'port'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_1.py:12: AttributeError
_______________________ test_add_host_to_existing_group ________________________

    def test_add_host_to_existing_group():
        inventory = InventoryData()
        inventory.add_group('webservers')
        added_host = inventory.add_host('web1', group='webservers')
        assert added_host == 'web1'
        assert 'web1' in inventory.hosts
        assert 'webservers' in inventory.groups
        assert inventory.hosts['web1'].name == 'web1'
>       assert inventory.hosts['web1'].port is None
E       AttributeError: 'Host' object has no attribute 'port'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_1.py:22: AttributeError
_______________________ test_add_host_with_specific_port _______________________

    def test_add_host_with_specific_port():
        inventory = InventoryData()
        inventory.add_group('dbservers')
        added_host = inventory.add_host('database1', group='dbservers', port=3306)
        assert added_host == 'database1'
        assert 'database1' in inventory.hosts
        assert 'dbservers' in inventory.groups
        assert inventory.hosts['database1'].name == 'database1'
>       assert inventory.hosts['database1'].port == 3306
E       AttributeError: 'Host' object has no attribute 'port'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_1.py:32: AttributeError
________________________ test_add_host_to_default_group ________________________

    def test_add_host_to_default_group():
        inventory = InventoryData()
        added_host = inventory.add_host('host2')
        assert added_host == 'host2'
        assert 'host2' in inventory.hosts
        assert 'ungrouped' in inventory.groups
        assert inventory.hosts['host2'].name == 'host2'
>       assert inventory.hosts['host2'].port is None
E       AttributeError: 'Host' object has no attribute 'port'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_1.py:41: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_1.py::test_add_host_without_group
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_1.py::test_add_host_to_existing_group
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_1.py::test_add_host_with_specific_port
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_1.py::test_add_host_to_default_group
============================== 4 failed in 0.47s ===============================
"""