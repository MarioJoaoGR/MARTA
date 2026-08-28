
import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.ini import InventoryModule

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_inventory_ini_InventoryModule__expand_hostpattern_1.py F [100%]

=================================== FAILURES ===================================
_____________ test_expand_hostpattern_invalid_contains_triple_dash _____________

    def test_expand_hostpattern_invalid_contains_triple_dash():
        inventory_module = InventoryModule()
>       with pytest.raises(AnsibleParserError) as e:
E       Failed: DID NOT RAISE <class 'ansible.errors.AnsibleParserError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_inventory_ini_InventoryModule__expand_hostpattern_1.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_inventory_ini_InventoryModule__expand_hostpattern_1.py::test_expand_hostpattern_invalid_contains_triple_dash
============================== 1 failed in 0.82s ===============================
"""