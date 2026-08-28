
import pytest
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
import os

@pytest.fixture(scope="module")
def playbook_executor():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='test_inventory')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    passwords = {}
    return PlaybookExecutor(playbooks=['dummy_playbook.yml'], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)

def test_generate_retry_inventory_success(playbook_executor):
    retry_path = 'test_retry_file'
    replay_hosts = ['host1', 'host2']
    assert playbook_executor._generate_retry_inventory(retry_path, replay_hosts) is True
    with open(retry_path, 'r') as fd:
        content = fd.read().strip()
        assert content == '\n'.join(replay_hosts)
    os.remove(retry_path)  # Clean up the test file

def test_generate_retry_inventory_failure(playbook_executor):
    retry_path = '/nonexistent/directory/test_retry_file'
    replay_hosts = ['host1', 'host2']
    assert playbook_executor._generate_retry_inventory(retry_path, replay_hosts) is False
