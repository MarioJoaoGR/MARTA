
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

# Test removing a file without recursion
def test_remove_file_without_recursion(shell_module):
    command = shell_module.remove("C:\\path\\to\\file")
    assert command == 'Remove-Item \'C:\\path\\to\\file\' -Force;', f"Command mismatch: expected '{'Remove-Item \'C:\\path\\to\\file\' -Force;'}' but got '{command}'"

# Test removing a directory with recursion
def test_remove_directory_with_recursion(shell_module):
    command = shell_module.remove("C:\\path\\to\\directory", recurse=True)
    assert command == 'Remove-Item \'C:\\path\\to\\directory\' -Force -Recurse;', f"Command mismatch: expected '{'Remove-Item \'C:\\path\\to\\directory\' -Force -Recurse;'}' but got '{command}'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: f-string expression part cannot include a backslash (line 12, col 167)
    assert command == 'Remove-Item \'C:\\path\\to\\file\' -Force;', f"Command mismatch: expected '{'Remove-Item \'C:\\path\\to\\file\' -Force;'}' but got '{command}'"
"""