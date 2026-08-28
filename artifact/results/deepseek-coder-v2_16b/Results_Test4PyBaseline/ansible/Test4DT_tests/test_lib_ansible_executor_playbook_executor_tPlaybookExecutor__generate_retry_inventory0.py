# Module: ansible.executor.playbook_executor
# test_playbook_executor.py
import os
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

def test_basic_initialization():
    inventory = InventoryManager(host_list='hosts')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()
    passwords = {}

    playbook_executor = PlaybookExecutor(playbooks=['playbook.yml'], 
                                          inventory=inventory, 
                                          variable_manager=variable_manager, 
                                          loader=loader, 
                                          passwords=passwords)
    
    assert isinstance(playbook_executor, PlaybookExecutor), "PlaybookExecutor instance should be created successfully"

def test_run_playbooks():
    inventory = InventoryManager(host_list='hosts')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()
    passwords = {}

    playbook_executor = PlaybookExecutor(playbooks=['playbook.yml'], 
                                          inventory=inventory, 
                                          variable_manager=variable_manager, 
                                          loader=loader, 
                                          passwords=passwords)
    
    result = playbook_executor.run()
    assert result is not None, "PlaybookExecutor run should return a result"

def test_generate_retry_inventory():
    inventory = InventoryManager(host_list='hosts')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()
    passwords = {}

    playbook_executor = PlaybookExecutor(playbooks=['playbook.yml'], 
                                          inventory=inventory, 
                                          variable_manager=variable_manager, 
                                          loader=loader, 
                                          passwords=passwords)
    
    failed_hosts = {'host1': 'unreachable'}
    retry_path = 'test_retryfile'
    success = playbook_executor._generate_retry_inventory(retry_path, list(failed_hosts.keys()))
    
    assert os.path.exists(retry_path), "Retry file should be created"
    with open(retry_path, 'r') as fd:
        content = fd.read().strip()
        assert content == 'host1', "Retry file should contain the failed host"
    assert success, "Generating retry inventory should succeed"

def test_handle_specific_cli_arguments():
    inventory = InventoryManager(host_list='hosts')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()
    passwords = {}

    playbook_executor = PlaybookExecutor(playbooks=['playbook.yml'], 
                                          inventory=inventory, 
                                          variable_manager=variable_manager, 
                                          loader=loader, 
                                          passwords=passwords,
                                          listhosts=True)
    
    assert playbook_executor._tqm is None, "PlaybookExecutor should handle --listhosts argument by setting _tqm to None"
