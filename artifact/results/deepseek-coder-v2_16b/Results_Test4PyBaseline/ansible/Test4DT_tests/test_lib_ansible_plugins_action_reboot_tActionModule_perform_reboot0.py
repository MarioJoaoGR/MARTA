# Module: ansible.plugins.action.reboot
import pytest
from ansible.plugins.action import ActionModule

# Fixture to create an instance of ActionModule for testing
@pytest.fixture
def action_module():
    return ActionModule()

# Test case for default reboot with a custom message
def test_perform_reboot_default(action_module):
    task_vars = {'msg': 'Reboot initiated by Ansible'}
    result = action_module.perform_reboot(task_vars, {'name': 'default'})
    assert not result['failed']
    assert result['rebooted']
    assert result['msg'] == "Reboot command failed. Error was: '{stdout}, {stderr}'".format(
        stdout='', stderr=''
    )

# Test case for reboot with specific delays and command
def test_perform_reboot_with_delays_and_command(action_module):
    task_vars = {
        'msg': 'Reboot initiated by Ansible',
        'pre_reboot_delay': 30,
        'reboot_command': 'shutdown -r now'
    }
    result = action_module.perform_reboot(task_vars, {'name': 'default'})
    assert not result['failed']
    assert result['rebooted']
    assert result['msg'] == "Reboot command failed. Error was: '{stdout}, {stderr}'".format(
        stdout='', stderr=''
    )

# Test case for shutdown instead of reboot
def test_perform_shutdown_instead_of_reboot(action_module):
    task_vars = {
        'msg': 'Shutting down system now',
        'pre_reboot_delay': 15,
        'reboot_command': 'shutdown -h now'
    }
    result = action_module.perform_reboot(task_vars, {'name': 'default'})
    assert not result['failed']
    assert not result['rebooted']
    assert result['msg'] == "Reboot command failed. Error was: '{stdout}, {stderr}'".format(
        stdout='', stderr=''
    )
