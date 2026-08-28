
import pytest
from ansible.plugins.shell import ShellModule
import base64

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()

# Test scenario 1: Valid input file should return a base64 encoded PowerShell script to compute SHA1 checksum
def test_valid_input_file(shell_module):
    path = 'example.txt'
    result = shell_module.checksum(path)
    assert isinstance(result, str), "Expected a string"
    decoded_script = base64.b64decode(result).decode('utf-8')
    assert 'If (Test-Path -PathType Leaf' in decoded_script, "Expected PowerShell script to check if file exists"
    assert '$fp' in decoded_script, "Expected PowerShell script to open the file"

# Test scenario 2: Valid input directory should return a base64 encoded PowerShell script checking if directory exists
def test_valid_input_directory(shell_module):
    path = 'example_dir'
    result = shell_module.checksum(path)
    assert isinstance(result, str), "Expected a string"
    decoded_script = base64.b64decode(result).decode('utf-8')
    assert 'If (Test-Path -PathType Container' in decoded_script, "Expected PowerShell script to check if directory exists"
    assert 'Write-Output "3"' in decoded_script, "Expected PowerShell script to output '3' for a directory"

# Test scenario 3: Invalid input with None type or non-existent path should return a base64 encoded PowerShell script checking if the path exists and output '1' for not found
def test_invalid_input_nonexistentpath(shell_module):
    path = None
    result = shell_module.checksum(path)
    assert isinstance(result, str), "Expected a string"
    decoded_script = base64.b64decode(result).decode('utf-8')
    assert 'If (Test-Path -PathType Container' not in decoded_script, "Expected PowerShell script to check if path exists"
    assert 'Write-Output "1"' in decoded_script, "Expected PowerShell script to output '1' for a non-existent path"
