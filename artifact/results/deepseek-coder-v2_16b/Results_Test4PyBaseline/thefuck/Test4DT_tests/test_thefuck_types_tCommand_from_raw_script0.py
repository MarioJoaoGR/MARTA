
import pytest
from thefuck.types import Command

# Test initialization with script and output
def test_command_initialization():
    cmd = Command("print('Hello, World!')", "Hello, World!")
    assert cmd.script == "print('Hello, World!')"
    assert cmd.output == "Hello, World!"

# Test creation from raw script parts
def test_command_from_raw_script():
    cmd = Command.from_raw_script(['echo', 'Hello, World!'])
    assert cmd.script == "echo Hello, World!"