
import pytest
from ansible.inventory.host import Host

# Test scenario 1: Test standard input with valid arguments
def test_valid_input_happy_path():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    assert isinstance(host._uuid, str)

# Test scenario 2: Test edge case with None values for initialization parameters
def test_edge_case_none_values():
    host = Host()
    assert host.name is None
    assert host.vars == {}
    assert host._uuid is None

# Test scenario 3: Test invalid input and error handling, such as non-integer port or missing name
def test_invalid_input_error_handling():
    with pytest.raises(TypeError):
        Host(name='exampleHost', port='invalid_port')
    
    with pytest.raises(TypeError):
        Host(name=None)
