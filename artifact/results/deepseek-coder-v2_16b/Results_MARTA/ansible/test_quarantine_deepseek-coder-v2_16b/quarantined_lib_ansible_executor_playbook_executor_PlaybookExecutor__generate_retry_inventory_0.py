
import pytest
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
import os

@pytest.fixture(scope="module")
def setup():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='test_inventory')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    passwords = {}
    playbooks = ['playbook1.yml', 'playbook2.yml']
    return PlaybookExecutor(playbooks=playbooks, inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__generate_retry_inventory_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_missing_lines ______________________________

setup = <ansible.executor.playbook_executor.PlaybookExecutor object at 0x7feec17e30d0>

    def test_missing_lines(setup):
        retry_path = "non_existent_file"
        replay_hosts = []
        result = setup._generate_retry_inventory(retry_path, replay_hosts)
>       assert not result, "Expected _generate_retry_inventory to return False for non-existent file"
E       AssertionError: Expected _generate_retry_inventory to return False for non-existent file
E       assert not True

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__generate_retry_inventory_0.py:22: AssertionError
---------------------------- Captured stderr setup -----------------------------
[WARNING]: Unable to parse /data/results/harness/sandbox/marta/test_inventory
as an inventory source
[WARNING]: No inventory was parsed, only implicit localhost is available
______________________________ test_invalid_input ______________________________

setup = <ansible.executor.playbook_executor.PlaybookExecutor object at 0x7feec17e30d0>

    def test_invalid_input(setup):
        retry_path = "/non/writable/file"
        replay_hosts = ["host1"]
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__generate_retry_inventory_0.py:27: Failed
----------------------------- Captured stderr call -----------------------------
[WARNING]: Could not create retry file '/non/writable/file'.         Unable to
create local directories(/non/writable): [Errno 30] Read-only file system:
b'/non'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__generate_retry_inventory_0.py::test_missing_lines
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__generate_retry_inventory_0.py::test_invalid_input
============================== 2 failed in 0.46s ===============================
"""