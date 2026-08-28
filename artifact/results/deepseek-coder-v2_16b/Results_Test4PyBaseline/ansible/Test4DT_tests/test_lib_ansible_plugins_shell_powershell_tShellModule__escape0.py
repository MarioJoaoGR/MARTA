
import pytest
from ansible.plugins.shell import powershell

# Create an instance of ShellModule for PowerShell
@pytest.fixture
def shell_module():
    return powershell.ShellModule()

@pytest.mark.parametrize("value, expected", [
    ("This is a 'test'.", "This is a ''\\''test\\'''."),
    ("Hello, World!", "Hello, World!"),  # No special characters to escape
    ("It's a test.", "It''\\''s a test."),  # Single quote needs escaping
    ("Über Über", "Über Über"),  # Non-ASCII characters are not escaped
])
def test_escape(shell_module, value, expected):
    assert shell_module._escape(value) == expected
