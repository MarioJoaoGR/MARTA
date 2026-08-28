
import pytest
from thefuck.rules.git_add_force import match
from thefuck.types import Command

# Test 1: No 'add' in script parts and no specific message in output
def test_no_match():
    command = Command(["echo", "Hello, World!"], "Use -f if you really want to add them.")
    assert not match(command)

# Test 2: 'add' in script parts but no specific message in output
def test_script_parts_but_no_message():
    command = Command(["git", "add", "-n"], "Everything up-to-date")
    assert not match(command)

# Test 3: No 'add' in script parts but specific message in output
def test_no_script_parts_but_message():
    command = Command([], "Use -f if you really want to add them.")
    assert not match(command)

# Test 4: Both 'add' in script parts and specific message in output