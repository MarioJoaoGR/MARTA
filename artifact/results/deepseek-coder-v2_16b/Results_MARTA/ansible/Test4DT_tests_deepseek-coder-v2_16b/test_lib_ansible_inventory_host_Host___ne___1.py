
import pytest
from ansible.inventory.host import Host

# Test valid inputs
def test_valid_inputs():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    assert isinstance(host._uuid, str)

# Test edge cases
def test_edge_cases():
    # None input
    with pytest.raises(TypeError):
        Host(name=None, port=None)
    
    # Empty list input
    host = Host(name='', port=0)
    assert host.name == ''
    assert host.vars['ansible_port'] == 0
    assert isinstance(host._uuid, str)

# Test raising exceptions for invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        Host()  # Missing required argument 'name'
