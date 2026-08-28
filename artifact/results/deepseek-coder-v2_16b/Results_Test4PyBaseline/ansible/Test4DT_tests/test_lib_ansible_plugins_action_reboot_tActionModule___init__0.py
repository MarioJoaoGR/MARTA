# Module: ansible.plugins.action.reboot
# Import the ActionModule class from the specified module
from ansible.plugins.action import ActionModule as Am

def test_basic_reboot():
    # Test initializing a basic reboot with default settings
    action_module = Am(msg='Reboot initiated by Ansible')
    assert hasattr(action_module, 'msg'), "Expected msg attribute to be set"
    assert hasattr(action_module, 'pre_reboot_delay'), "Expected pre_reboot_delay attribute to be set"
    assert action_module.pre_reboot_delay == 0, "Expected default pre_reboot_delay to be 0"
    assert action_module.reboot_command == 'shutdown -r now', "Expected default reboot_command to be 'shutdown -r now'"

def test_custom_reboot():
    # Test initializing a reboot with custom pre-reboot delay and message
    action_module = Am(msg='Rebooting system now', pre_reboot_delay=30)
    assert hasattr(action_module, 'msg'), "Expected msg attribute to be set"
    assert action_module.msg == 'Rebooting system now', "Expected custom msg to be set"
    assert action_module.pre_reboot_delay == 30, "Expected pre_reboot_delay to be 30"
    assert action_module.reboot_command == 'shutdown -r now', "Expected default reboot_command to be 'shutdown -r now'"

def test_custom_reboot_command():
    # Test initializing a reboot with custom command and message
    action_module = Am(msg='Rebooting system now', pre_reboot_delay=15, reboot_command='shutdown -r now')
    assert hasattr(action_module, 'msg'), "Expected msg attribute to be set"
    assert action_module.msg == 'Rebooting system now', "Expected custom msg to be set"
    assert action_module.pre_reboot_delay == 15, "Expected pre_reboot_delay to be 15"
    assert action_module.reboot_command == 'shutdown -r now', "Expected reboot_command to be 'shutdown -r now'"

def test_custom_post_reboot_delay():
    # Test initializing a reboot with custom post-reboot delay and message
    action_module = Am(msg='System will reboot in 60 seconds', pre_reboot_delay=0, post_reboot_delay=60, reboot_command='shutdown -r now')
    assert hasattr(action_module, 'msg'), "Expected msg attribute to be set"
    assert action_module.msg == 'System will reboot in 60 seconds', "Expected custom msg to be set"
    assert action_module.pre_reboot_delay == 0, "Expected pre_reboot_delay to be 0"
    assert action_module.post_reboot_delay == 60, "Expected post_reboot_delay to be 60"
    assert action_module.reboot_command == 'shutdown -r now', "Expected reboot_command to be 'shutdown -r now'"

def test_basic_shutdown():
    # Test initializing a basic shutdown with default settings
    action_module = Am(msg='Shutting down system now', pre_reboot_delay=15, reboot_command='shutdown -h now')
    assert hasattr(action_module, 'msg'), "Expected msg attribute to be set"
    assert hasattr(action_module, 'pre_reboot_delay'), "Expected pre_reboot_delay attribute to be set"
    assert action_module.pre_reboot_delay == 15, "Expected default pre_reboot_delay to be 15"
    assert action_module.reboot_command == 'shutdown -h now', "Expected default reboot_command to be 'shutdown -h now'"

def test_custom_shutdown():
    # Test initializing a shutdown with custom pre-reboot delay and message
    action_module = Am(msg='Shutting down system now', pre_reboot_delay=15, reboot_command='shutdown -h now')
    assert hasattr(action_module, 'msg'), "Expected msg attribute to be set"
    assert action_module.msg == 'Shutting down system now', "Expected custom msg to be set"
    assert action_module.pre_reboot_delay == 15, "Expected pre_reboot_delay to be 15"
    assert action_module.reboot_command == 'shutdown -h now', "Expected reboot_command to be 'shutdown -h now'"

def test_custom_shutdown_command():
    # Test initializing a shutdown with custom command and message
    action_module = Am(msg='System will shut down in 30 seconds', pre_reboot_delay=0, reboot_command='shutdown -h now')
    assert hasattr(action_module, 'msg'), "Expected msg attribute to be set"
    assert action_module.msg == 'System will shut down in 30 seconds', "Expected custom msg to be set"
    assert action_module.pre_reboot_delay == 0, "Expected pre_reboot_delay to be 0"
    assert action_module.reboot_command == 'shutdown -h now', "Expected reboot_command to be 'shutdown -h now'"
