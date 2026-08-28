
import pytest
from ansible.inventory.host import Host

# Test valid inputs for Host initialization and serialization
def test_valid_inputs():
    host = Host(name='exampleHost', port=22)
    assert host.name == 'exampleHost'
    assert host.vars['ansible_port'] == 22
    serialized_host = host.serialize()
    assert isinstance(serialized_host, dict)
    assert serialized_host['name'] == 'exampleHost'
    assert serialized_host['vars']['ansible_port'] == 22

# Test edge cases for Host initialization
def test_edge_cases():
    host = Host(name=None, port=0, gen_uuid=False)
    assert host.name is None
    assert 'ansible_port' not in host.vars
    assert host._uuid is None
    assert host.implicit is False

# Test invalid inputs and error handling for Host initialization
def test_invalid_inputs():
    with pytest.raises(TypeError):
        host = Host(name='exampleHost', port='not_a_port')
