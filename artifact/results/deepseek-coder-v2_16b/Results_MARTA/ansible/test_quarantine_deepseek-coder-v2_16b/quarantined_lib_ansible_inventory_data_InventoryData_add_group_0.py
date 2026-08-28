
import pytest
from ansible.inventory.data import InventoryData

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_group_0.py F [100%]

=================================== FAILURES ===================================
_________________________ test_add_group_invalid_empty _________________________

    def test_add_group_invalid_empty():
        inventory = InventoryData()
        with pytest.raises(Exception) as e:
            inventory.add_group('')
>       assert str(e.value) == "Invalid empty/false group name provided: None"
E       AssertionError: assert 'Invalid empt...me provided: ' == 'Invalid empt...rovided: None'
E         
E         - Invalid empty/false group name provided: None
E         ?                                          ----
E         + Invalid empty/false group name provided:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_group_0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_group_0.py::test_add_group_invalid_empty
============================== 1 failed in 0.42s ===============================
"""