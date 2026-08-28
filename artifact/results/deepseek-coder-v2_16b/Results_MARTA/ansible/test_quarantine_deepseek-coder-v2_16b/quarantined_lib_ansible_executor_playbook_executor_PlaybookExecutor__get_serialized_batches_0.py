
import pytest
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

@pytest.fixture(scope="module")
def playbook_executor():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='inventory_file')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    passwords = {}  # If you have any passwords, include them here
    return PlaybookExecutor(playbooks=['playbook1.yml', 'playbook2.yml'], 
                             inventory=inventory, 
                             variable_manager=variable_manager, 
                             loader=loader, 
                             passwords=passwords)



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__get_serialized_batches_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_get_serialized_batches_valid _______________________

playbook_executor = <ansible.executor.playbook_executor.PlaybookExecutor object at 0x7f02503c3f40>

    def test_get_serialized_batches_valid(playbook_executor):
        play = {
            'hosts': ['host1', 'host2', 'host3'],
            'serial': [2]
        }
>       serialized_batches = playbook_executor._get_serialized_batches(play)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__get_serialized_batches_0.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.executor.playbook_executor.PlaybookExecutor object at 0x7f02503c3f40>
play = {'hosts': ['host1', 'host2', 'host3'], 'serial': [2]}

    def _get_serialized_batches(self, play):
        '''
        Returns a list of hosts, subdivided into batches based on
        the serial size specified in the play.
        '''
    
        # make sure we have a unique list of hosts
>       all_hosts = self._inventory.get_hosts(play.hosts, order=play.order)
E       AttributeError: 'dict' object has no attribute 'hosts'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/playbook_executor.py:282: AttributeError
---------------------------- Captured stderr setup -----------------------------
[WARNING]: Unable to parse /data/results/harness/sandbox/marta/inventory_file
as an inventory source
[WARNING]: No inventory was parsed, only implicit localhost is available
__________________ test_get_serialized_batches_invalid_serial __________________

playbook_executor = <ansible.executor.playbook_executor.PlaybookExecutor object at 0x7f02503c3f40>

    def test_get_serialized_batches_invalid_serial(playbook_executor):
        play = {
            'hosts': ['host1', 'host2', 'host3'],
            'serial': [0]
        }
        with pytest.raises(ValueError):
>           playbook_executor._get_serialized_batches(play)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__get_serialized_batches_0.py:35: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.executor.playbook_executor.PlaybookExecutor object at 0x7f02503c3f40>
play = {'hosts': ['host1', 'host2', 'host3'], 'serial': [0]}

    def _get_serialized_batches(self, play):
        '''
        Returns a list of hosts, subdivided into batches based on
        the serial size specified in the play.
        '''
    
        # make sure we have a unique list of hosts
>       all_hosts = self._inventory.get_hosts(play.hosts, order=play.order)
E       AttributeError: 'dict' object has no attribute 'hosts'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/playbook_executor.py:282: AttributeError
____________________ test_get_serialized_batches_no_serial _____________________

playbook_executor = <ansible.executor.playbook_executor.PlaybookExecutor object at 0x7f02503c3f40>

    def test_get_serialized_batches_no_serial(playbook_executor):
        play = {
            'hosts': ['host1', 'host2', 'host3']
        }
>       serialized_batches = playbook_executor._get_serialized_batches(play)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__get_serialized_batches_0.py:41: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.executor.playbook_executor.PlaybookExecutor object at 0x7f02503c3f40>
play = {'hosts': ['host1', 'host2', 'host3']}

    def _get_serialized_batches(self, play):
        '''
        Returns a list of hosts, subdivided into batches based on
        the serial size specified in the play.
        '''
    
        # make sure we have a unique list of hosts
>       all_hosts = self._inventory.get_hosts(play.hosts, order=play.order)
E       AttributeError: 'dict' object has no attribute 'hosts'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/playbook_executor.py:282: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__get_serialized_batches_0.py::test_get_serialized_batches_valid
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__get_serialized_batches_0.py::test_get_serialized_batches_invalid_serial
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_playbook_executor_PlaybookExecutor__get_serialized_batches_0.py::test_get_serialized_batches_no_serial
============================== 3 failed in 0.76s ===============================
"""