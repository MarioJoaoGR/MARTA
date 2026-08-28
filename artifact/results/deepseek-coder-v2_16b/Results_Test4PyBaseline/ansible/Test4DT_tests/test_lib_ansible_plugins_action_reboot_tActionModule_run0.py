# Module: ansible.plugins.action.reboot
import pytest
from ansible.plugins.action import ActionModule

# Fixture to create an instance of ActionModule for testing
@pytest.fixture
def action_module():
    return ActionModule(msg='Rebooting system now', pre_reboot_delay=30, reboot_command='shutdown -r now')

# Test case for initiating a reboot with custom message and delays
def test_initiate_reboot_with_custom_message_and_delays(action_module):
    result = action_module.run()
    assert 'changed' in result, "Expected 'changed' to be in the result"
    assert 'elapsed' in result, "Expected 'elapsed' to be in the result"
    assert 'rebooted' in result, "Expected 'rebooted' to be in the result"
    assert not result['failed'], "Expected no failure in the reboot process"
    assert result['msg'] == 'Rebooting system now', "Expected custom message during reboot"

# Test case for performing a shutdown instead of a reboot
def test_perform_shutdown(monkeypatch):
    monkeypatch.setattr(ActionModule, 'DEFAULT_SHUTDOWN_COMMAND', 'shutdown -h now')
    action_module = ActionModule(msg='Shutting down system now', pre_reboot_delay=15, reboot_command='shutdown -h now')
    result = action_module.run()
    assert 'changed' in result, "Expected 'changed' to be in the result"
    assert 'elapsed' in result, "Expected 'elapsed' to be in the result"
    assert 'rebooted' in result, "Expected 'rebooted' to be in the result"
    assert not result['failed'], "Expected no failure in the shutdown process"
    assert result['msg'] == 'Shutting down system now', "Expected custom message during shutdown"

# Test case for using default arguments with no customization
def test_default_arguments():
    action_module = ActionModule()
    result = action_module.run()
    assert 'changed' in result, "Expected 'changed' to be in the result"
    assert 'elapsed' in result, "Expected 'elapsed' to be in the result"
    assert 'rebooted' in result, "Expected 'rebooted' to be in the result"
    assert not result['failed'], "Expected no failure in the default reboot process"
    assert result['msg'] == 'Reboot initiated by Ansible', "Expected default message during reboot"

# Test case for specifying custom boot time command and timeout
def test_custom_boot_time_command_and_timeout():
    action_module = ActionModule(boot_time_command='cat /proc/sys/kernel/random/boot_id', reboot_timeout=900)
    result = action_module.run()
    assert 'changed' in result, "Expected 'changed' to be in the result"
    assert 'elapsed' in result, "Expected 'elapsed' to be in the result"
    assert 'rebooted' in result, "Expected 'rebooted' to be in the result"
    assert not result['failed'], "Expected no failure in the reboot process with custom timeout"
    assert action_module.boot_time_command == 'cat /proc/sys/kernel/random/boot_id', "Expected custom boot time command to be set"
    assert action_module.reboot_timeout == 900, "Expected custom reboot timeout to be set"

# Test case for using check mode to simulate an action
def test_check_mode(monkeypatch):
    monkeypatch.setattr(ActionModule, '_play_context', type('PlayContext', (object,), {'check_mode': True})())
    action_module = ActionModule()
    result = action_module.run()
    assert 'changed' in result, "Expected 'changed' to be in the result when in check mode"
    assert 'elapsed' in result, "Expected 'elapsed' to be in the result when in check mode"
    assert 'rebooted' in result, "Expected 'rebooted' to be in the result when in check mode"
    assert not result['failed'], "Expected no failure in the action when in check mode"
