# Module: ansible.plugins.action.reboot
# test_action_module.py
from ansible.plugins.action import ActionModule
import pytest

@pytest.fixture
def action_module():
    return ActionModule(task={}, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_init_with_default_values(action_module):
    action_module = ActionModule(msg='Rebooting system now', pre_reboot_delay=30, reboot_command='shutdown -r now')
    assert action_module.args == {
        'boot_time_command': 'cat /proc/sys/kernel/random/boot_id',
        'connect_timeout': None,
        'msg': 'Rebooting system now',
        'post_reboot_delay': 0,
        'pre_reboot_delay': 30,
        'reboot_command': 'shutdown -r now',
        'reboot_timeout': 600,
        'search_paths': [],
        'test_command': 'whoami'
    }

def test_init_with_custom_values(action_module):
    action_module = ActionModule(msg='Custom message', pre_reboot_delay=15, reboot_command='custom_shutdown -r now')
    assert action_module.args == {
        'boot_time_command': 'cat /proc/sys/kernel/random/boot_id',
        'connect_timeout': None,
        'msg': 'Custom message',
        'post_reboot_delay': 0,
        'pre_reboot_delay': 15,
        'reboot_command': 'custom_shutdown -r now',
        'reboot_timeout': 600,
        'search_paths': [],
        'test_command': 'whoami'
    }

def test_check_delay_positive(action_module):
    assert action_module._check_delay('pre_reboot_delay', 0) == 30

def test_check_delay_zero(action_module):
    assert action_module._check_delay('post_reboot_delay', 0) == 0

def test_check_delay_negative(action_module):
    assert action_module._check_delay('pre_reboot_delay', 0) == 30

if __name__ == '__main__':
    pytest.main()
