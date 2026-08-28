
from ansible.plugins.shell.powershell import ShellModule
import pytest
import base64
import os

def test_encode_script_with_valid_input():
    shell_module = ShellModule()
    script = "Write-Output 'Hello, World!'"
    encoded_script = shell_module._encode_script(script)
    assert isinstance(encoded_script, str), "Expected a string but got something else"
    assert len(encoded_script) > 0, "Encoded script should not be empty"



