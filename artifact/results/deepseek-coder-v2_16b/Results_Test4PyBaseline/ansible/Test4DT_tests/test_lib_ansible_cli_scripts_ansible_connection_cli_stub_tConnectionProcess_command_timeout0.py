# Module: ansible.cli.scripts.ansible_connection_cli_stub
# test_connection_process.py
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.plugins.loader import init_plugin_loader
import signal
import os

@pytest.fixture(scope="module")
def setup():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    playbook = Play().load({'name': 'MyPlay', 'hosts': 'localhost', 'tasks': []}, variable_manager=variable_manager, loader=loader)
    tqm = TaskQueueManager(play=playbook, variable_manager=variable_manager, loader=loader, options={}, stdout_callback='default')
    fd = open('output.json', 'w+')
    cp = ConnectionProcess(fd=fd, play_context=tqm.get_play().get_context(), socket_path='unix:/tmp/ansible.sock', original_path='/original/task/path')
    yield cp
    fd.close()

def test_basic_usage(setup):
    cp = setup
    with pytest.raises(Exception) as excinfo:
        cp.start({'var1': 'value1'})
    assert str(excinfo.value) == f'command timeout triggered, timeout value is {cp.connection.get_option("persistent_command_timeout")} secs.\nSee the timeout setting options in the Network Debug and Troubleshooting Guide.'

def test_usage_with_task_uuid_and_playbook_pid(setup):
    cp = setup
    cp._task_uuid = '1234-5678-90AB'
    cp._ansible_playbook_pid = os.getpid()
    with pytest.raises(Exception) as excinfo:
        cp.start({'var1': 'value1'})
    assert str(excinfo.value) == f'command timeout triggered, timeout value is {cp.connection.get_option("persistent_command_timeout")} secs.\nSee the timeout setting options in the Network Debug and Troubleshooting Guide.'

def test_handling_command_timeout(setup):
    cp = setup
    signal.signal(signal.SIGALRM, cp.command_timeout)
    signal.alarm(10)  # Set a 10-second alarm for the command execution
    with pytest.raises(Exception) as excinfo:
        cp.start({'var1': 'value1'})
    assert str(excinfo.value) == f'command timeout triggered, timeout value is {cp.connection.get_option("persistent_command_timeout")} secs.\nSee the timeout setting options in the Network Debug and Troubleshooting Guide.'
