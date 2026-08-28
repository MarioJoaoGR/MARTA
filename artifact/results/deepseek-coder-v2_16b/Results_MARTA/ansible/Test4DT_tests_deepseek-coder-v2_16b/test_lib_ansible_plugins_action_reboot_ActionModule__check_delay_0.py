
import pytest
from ansible.plugins.action import reboot

# Test valid inputs scenario
def test_valid_inputs():
    action = reboot()
    task_vars = {
        'boot_time_command': 'cat /proc/sys/kernel/random/boot_id',
        'msg': 'Reboot initiated by Ansible',
        'pre_reboot_delay': 10,
        'post_reboot_delay': 20,
        'reboot_timeout': 300,
        'connect_timeout': 60,
        'test_command': 'whoami'
    }
    
    result = action.run(task_vars=task_vars)
    
    assert result['changed'] is True
    assert result['rebooted'] is True or result['shutdown'] is True

# Test edge cases scenario
def test_edge_cases():
    action = reboot()
    task_vars = {
        'boot_time_command': None,
        'msg': '',
        'pre_reboot_delay': -10,
        'post_reboot_delay': 0,
        'reboot_timeout': 600,
        'connect_timeout': None,
        'test_command': None
    }
    
    result = action.run(task_vars=task_vars)
    
    assert result['changed'] is True
    assert result['rebooted'] is True or result['shutdown'] is True

# Test invalid inputs scenario
def test_invalid_inputs():
    action = reboot()
    task_vars = {
        'boot_time_command': 'invalid_command',
        'msg': 123,
        'pre_reboot_delay': 'ten',
        'post_reboot_delay': -20,
        'reboot_timeout': 'three hundred',
        'connect_timeout': 'sixty',
        'test_command': []
    }
    
    with pytest.raises(ValueError):
        action.run(task_vars=task_vars)
