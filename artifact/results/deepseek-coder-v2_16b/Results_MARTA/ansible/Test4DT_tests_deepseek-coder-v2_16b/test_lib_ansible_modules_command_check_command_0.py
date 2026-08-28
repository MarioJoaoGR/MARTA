
import pytest
from ansible.modules.command import check_command
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture(scope="function")
def module():
    return AnsibleModule({}, no_log=True)

# Test Scenario 1: test_valid_input_string
def test_valid_input_string(module):
    commandline = 'ls -l'
    check_command(module, commandline)
    assert module.warnings == [f"Consider using the file module with {arguments['ls']} rather than running '{command}'.  If you need to use 'ls' because the {mod} module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."]

# Test Scenario 2: test_valid_input_list
def test_valid_input_list(module):
    commandline = ['tar', '--extract']
    check_command(module, commandline)
    assert module.warnings == [f"Consider using the {commands['tar']} rather than running 'tar'.  If you need to use 'tar' because the {mod} module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."]

# Test Scenario 3: test_invalid_command
def test_invalid_command(module):
    commandline = 'unknown_command'
    check_command(module, commandline)
    assert module.warnings == []
