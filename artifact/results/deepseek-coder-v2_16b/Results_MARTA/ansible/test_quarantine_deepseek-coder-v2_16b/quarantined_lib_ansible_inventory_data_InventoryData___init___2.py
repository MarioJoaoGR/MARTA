
import pytest
from ansible.inventory.data import InventoryData

# Test adding a child to an existing group
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData___init___2.py F [100%]

=================================== FAILURES ===================================
_______________________ test_add_child_to_existing_group _______________________

    def test_add_child_to_existing_group():
        inventory = InventoryData()
        inventory.add_group('test_group')
>       assert inventory.add_child('test_group', 'localhost') == True

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData___init___2.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.inventory.data.InventoryData object at 0x7fca8367c520>
group = 'test_group', child = 'localhost'

    def add_child(self, group, child):
        ''' Add host or group to group '''
        added = False
        if group in self.groups:
            g = self.groups[group]
            if child in self.groups:
                added = g.add_child_group(self.groups[child])
            elif child in self.hosts:
                added = g.add_host(self.hosts[child])
            else:
>               raise AnsibleError("%s is not a known host nor group" % child)
E               ansible.errors.AnsibleError: localhost is not a known host nor group

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/inventory/data.py:268: AnsibleError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData___init___2.py::test_add_child_to_existing_group
============================== 1 failed in 0.81s ===============================
"""