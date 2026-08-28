
import pytest
from ansible.inventory.host import Host

# Test scenario 1: Test standard input with only a name
def test_valid_input_with_name():
    host = Host(name='exampleHost')
    assert host.name == 'exampleHost'
    assert host._uuid is not None, "UUID should be generated for valid input"

# Test scenario 2: Test edge case without generating a unique identifier
def test_edge_case_no_gen_uuid():
    host = Host(name='exampleHost', gen_uuid=False)
    assert host.name == 'exampleHost'
    assert host._uuid is None, "UUID should not be generated for edge case"

# Test scenario 3: Test invalid input with missing name
def test_invalid_input_missing_name():
    try:
        host = Host()
    except TypeError as e:
        assert str(e) == "'Host' object initialization takes exactly 1 or 3 arguments (0 given)", "Expected TypeError for missing name"
