
import pytest
from thefuck.types import Command

# Test valid case
def test_valid_case():
    cmd = Command(script='print("Hello, World!")', output='Hello, World!')
    assert cmd.script == 'print("Hello, World!")'
    assert cmd.output == 'Hello, World!'

# Test edge case
def test_edge_case():
    cmd = Command(script='', output='')
    assert cmd.script == ''
    assert cmd.output == ''

# Test invalid input causing exception
def test_invalid_input():
    with pytest.raises(TypeError):
        Command()
