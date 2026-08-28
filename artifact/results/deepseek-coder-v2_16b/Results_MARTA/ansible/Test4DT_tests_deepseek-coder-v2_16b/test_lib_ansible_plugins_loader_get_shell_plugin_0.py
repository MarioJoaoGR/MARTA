
import pytest
from ansible.plugins.loader import get_shell_plugin
from ansible.errors import AnsibleError
import os
from collections import namedtuple

# Define a simple shell type and executable for testing
Shell = namedtuple('Shell', ['SHELL_FAMILY'])
shell_loader = {
    'sh': Shell(SHELL_FAMILY='sh'),
    'csh': Shell(SHELL_FAMILY='csh')
}

# Mock the shell_loader for testing


def test_get_shell_plugin_specified_executable():
    shell = get_shell_plugin(executable='/bin/bash')
    assert hasattr(shell, 'executable') and shell.executable == '/bin/bash'