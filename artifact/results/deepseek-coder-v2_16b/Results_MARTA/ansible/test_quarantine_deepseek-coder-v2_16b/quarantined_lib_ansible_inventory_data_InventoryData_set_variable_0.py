
import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_set_variable_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        inventory = InventoryData()
        group_name = inventory.add_group('webservers')
        assert group_name == 'webservers'
    
        # Add a host to the group
>       added = inventory.add_child('webservers', 'host1')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_set_variable_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.inventory.data.InventoryData object at 0x7f48748276d0>
group = 'webservers', child = 'host1'

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
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        inventory = InventoryData()
        with pytest.raises(AnsibleError) as e_info:
            inventory.add_child('non_existent_group', 'host1')
    
>       assert str(e_info.value).startswith("Could not identify group or host named non_existent_group"), \
               f"Expected error message to start with 'Could not identify group or host named non_existent_group', but got {str(e_info.value)}"
E       AssertionError: Expected error message to start with 'Could not identify group or host named non_existent_group', but got non_existent_group is not a known group
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7f48746fa9d0>('Could not identify group or host named non_existent_group')
E        +    where <built-in method startswith of str object at 0x7f48746fa9d0> = 'non_existent_group is not a known group'.startswith
E        +      where 'non_existent_group is not a known group' = str(non_existent_group is not a known group)
E        +        where non_existent_group is not a known group = <ExceptionInfo non_existent_group is not a known group tblen=2>.value

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_set_variable_0.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_set_variable_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_set_variable_0.py::test_invalid_input
============================== 2 failed in 0.48s ===============================
"""