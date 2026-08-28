
import pytest
from ansible.inventory.host import Host
import uuid

# Helper function to generate a unique UUID for testing
def get_unique_id():
    return str(uuid.uuid4())

# Scenario 1: Test standard input with valid parameters
def test_valid_input_happy_path():
    host = Host(name='exampleHost', port=22, gen_uuid=True)
    assert host.name == 'exampleHost'
    assert host.address == 'exampleHost'
    assert isinstance(host._uuid, str)
    assert host.vars['ansible_port'] == 22

# Scenario 2: Test edge cases such as None or empty values
def test_edge_cases():
    with pytest.raises(TypeError):
        Host(name=None)
    with pytest.raises(TypeError):
        Host(port='')
    host = Host(name='exampleHost', port=None, gen_uuid=False)
    assert host.name == 'exampleHost'
    assert host.address == 'exampleHost'
    assert host._uuid is None
    assert 'ansible_port' not in host.vars

# Scenario 3: Test invalid inputs and error handling
def test_invalid_inputs():
    with pytest.raises(ValueError):
        Host(name='', port=-1, gen_uuid=True)
    with pytest.raises(TypeError):
        Host(name=None, port=22, gen_uuid=False)
