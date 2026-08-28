
import pytest
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
import os

@pytest.fixture(scope="module")
def setup():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='inventory_file')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    passwords = {}  # If you have any passwords, include them here
    playbook_executor = PlaybookExecutor(playbooks=['/path/to/playbook1.yml', '/path/to/playbook2.yml'], 
                                          inventory=inventory, 
                                          variable_manager=variable_manager, 
                                          loader=loader, 
                                          passwords=passwords)
    return playbook_executor

def test_generate_retry_inventory_success(setup):
    retry_path = '/tmp/retry_file'
    replay_hosts = ['host1', 'host2']
    result = setup._generate_retry_inventory(retry_path, replay_hosts)
    assert result is True
    with open(retry_path, 'r') as fd:
        content = fd.read().strip()
    assert content == '\n'.join(replay_hosts)
    os.remove(retry_path)  # Clean up the temporary file

def test_generate_retry_inventory_failure(setup):
    retry_path = '/nonexistent/directory/retry_file'
    replay_hosts = ['host1', 'host2']
    result = setup._generate_retry_inventory(retry_path, replay_hosts)
    assert result is False
