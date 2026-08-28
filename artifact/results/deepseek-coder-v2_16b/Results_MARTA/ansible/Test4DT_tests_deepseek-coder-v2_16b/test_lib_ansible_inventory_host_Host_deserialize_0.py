
import pytest
from ansible.inventory.host import Host

# Test valid inputs for Host initialization and deserialization
def test_valid_inputs():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.address == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    assert isinstance(host._uuid, str)
    
    # Test deserialization
    data = {'name': 'exampleHost', 'vars': {'ansible_port': 22}, 'address': '', 'uuid': None, 'implicit': False}
    host.deserialize(data)
    assert host.name == 'exampleHost'
    assert host.address == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    assert isinstance(host._uuid, str)

# Test edge cases such as None, empty lists, boundary values
def test_edge_cases():
    with pytest.raises(TypeError):
        Host()  # Should raise TypeError because not enough arguments provided
    
    host = Host(name=None)
    assert host.name is None
    assert host.address is None
    assert 'ansible_port' not in host.vars
    assert host._uuid is None
    
    data = {'name': None, 'vars': {}, 'address': '', 'uuid': None, 'implicit': False}
    host.deserialize(data)
    assert host.name is None
    assert host.address is None
    assert not host.vars
    assert host._uuid is None

# Test invalid inputs and error handling scenarios
def test_invalid_inputs():
    with pytest.raises(TypeError):
        Host(name=123, port='string')  # Should raise TypeError because of incompatible types
    
    with pytest.raises(ValueError):
        Host(name='exampleHost', port=-1)  # Should raise ValueError because port is negative
    
    data = {'name': 'invalidName', 'vars': {}, 'address': '', 'uuid': None, 'implicit': False}
    host = Host()
    with pytest.raises(KeyError):
        host.deserialize(data)  # Should raise KeyError because of invalid data structure
