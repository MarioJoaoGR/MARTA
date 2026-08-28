# Module: ansible.plugins.action.reboot
# test_action_module.py
from ansible.plugins.action import ActionModule as AnsibleActionModule
import pytest

@pytest.fixture
def action_module():
    args = {
        'msg': 'Rebooting system now',
        'pre_reboot_delay': 30,
        'reboot_command': 'shutdown -r now'
    }
    kwargs = {}
    return AnsibleActionModule(argument_spec=args, **kwargs)

def test_init_with_custom_settings(action_module):
    assert action_module.msg == 'Rebooting system now'
    assert action_module.pre_reboot_delay == 30
    assert action_module.reboot_command == 'shutdown -r now'

def test_init_without_custom_settings(action_module):
    args = {
        'msg': 'Reboot initiated by Ansible'
    }
    kwargs = {}
    action_module_no_args = AnsibleActionModule(argument_spec=args, **kwargs)
    assert action_module_no_args.msg == 'Reboot initiated by Ansible'
    assert action_module_no_args.pre_reboot_delay == 0
    assert action_module_no_args.reboot_command is None

def test_get_shutdown_command_with_custom_path(action_module):
    task_vars = {}
    distribution = 'freebsd'
    command = action_module.get_shutdown_command(task_vars, distribution)
    assert command == '/sbin/sysctl kern.boottime'

def test_get_shutdown_command_without_custom_path(action_module):
    task_vars = {}
    distribution = 'openbsd'
    command = action_module.get_shutdown_command(task_vars, distribution)
    assert command == '/sbin/sysctl kern.boottime'

def test_get_shutdown_command_invalid_reboot_command():
    args = {
        'msg': 'Rebooting system now',
        'pre_reboot_delay': 30,
        'reboot_command': 'invalid_command'
    }
    with pytest.raises(AnsibleError):
        AnsibleActionModule(argument_spec=args)

def test_get_shutdown_command_with_search_paths():
    task_vars = {}
    distribution = 'linux'
    action_module.task.args['search_paths'] = ['/usr/local/sbin', '/usr/local/bin']
    command = action_module.get_shutdown_command(task_vars, distribution)
    assert command == '/usr/local/sbin/shutdown'  # Assuming the path is found in these paths
