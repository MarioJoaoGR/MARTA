
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_remove_host_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________________ test_remove_existing_host ___________________________

    def test_remove_existing_host():
        inventory = InventoryData()
        host1 = Host('host1')
        with pytest.raises(TypeError):
>           inventory.add_host(host1)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_remove_host_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.inventory.data.InventoryData object at 0x7f2c0631cfd0>
host = host1, group = None, port = None

    def add_host(self, host, group=None, port=None):
        ''' adds a host to inventory and possibly a group if not there already '''
    
        if host:
            if not isinstance(host, string_types):
>               raise AnsibleError("Invalid host name supplied, expected a string but got %s for %s" % (type(host), host))
E               ansible.errors.AnsibleError: Invalid host name supplied, expected a string but got <class 'ansible.inventory.host.Host'> for host1

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/inventory/data.py:196: AnsibleError
________________________ test_remove_non_existing_host _________________________

    def test_remove_non_existing_host():
        inventory = InventoryData()
        host1 = Host('host1')
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_remove_host_0.py:14: Failed
_________________________ test_remove_host_from_group __________________________

    def test_remove_host_from_group():
        inventory = InventoryData()
        group1 = 'group1'
        host1 = Host('host1')
    
        inventory.add_group(group1)
>       inventory.add_child(group1, host1)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_remove_host_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.inventory.data.InventoryData object at 0x7f2c0610c5b0>
group = 'group1', child = host1

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
E               ansible.errors.AnsibleError: host1 is not a known host nor group

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/inventory/data.py:268: AnsibleError
_______________________ test_remove_host_from_all_groups _______________________

    def test_remove_host_from_all_groups():
        inventory = InventoryData()
        host1 = Host('host1')
    
        inventory.add_group('group1')
>       inventory.add_child('group2', host1)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_remove_host_0.py:37: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.inventory.data.InventoryData object at 0x7f2c0631f820>
group = 'group2', child = host1

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
                raise AnsibleError("%s is not a known host nor group" % child)
            self._groups_dict_cache = {}
            display.debug('Group %s now contains %s' % (group, child))
        else:
>           raise AnsibleError("%s is not a known group" % group)
E           ansible.errors.AnsibleError: group2 is not a known group

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/inventory/data.py:272: AnsibleError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_remove_host_0.py::test_remove_existing_host
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_remove_host_0.py::test_remove_non_existing_host
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_remove_host_0.py::test_remove_host_from_group
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_remove_host_0.py::test_remove_host_from_all_groups
============================== 4 failed in 0.45s ===============================
"""