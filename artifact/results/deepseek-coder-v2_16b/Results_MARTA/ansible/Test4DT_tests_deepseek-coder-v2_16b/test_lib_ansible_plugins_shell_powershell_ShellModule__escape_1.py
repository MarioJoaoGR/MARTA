
import pytest
from ansible.plugins.shell.powershell import ShellModule
import re

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()

def test_escape_basic(shell_module):
    value = "This is a 'test'."
    escaped_value = shell_module._escape(value)
    assert escaped_value == "This is a ''test''."

def test_escape_special_chars(shell_module):
    special_chars = ["'", '\u2018', '\u2019', '\u201a', '\u201b']
    for char in special_chars:
        value = f"This is a {char} test."
        escaped_value = shell_module._escape(value)
        assert escaped_value == f"This is a {char}{char} test."
