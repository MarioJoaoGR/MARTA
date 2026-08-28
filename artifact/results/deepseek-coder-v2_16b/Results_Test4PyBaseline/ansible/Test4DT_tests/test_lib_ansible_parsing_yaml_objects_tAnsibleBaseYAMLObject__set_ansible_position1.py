
import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

# Test fixture to create an instance of AnsibleBaseYAMLObject for each test
@pytest.fixture
def base_object():
    return AnsibleBaseYAMLObject()

# Test setting a valid position information
def test_set_valid_position(base_object):
    base_object._set_ansible_position(('source_code', 10, 3))
    assert base_object._data_source == 'source_code'
    assert base_object._line_number == 10
    assert base_object._column_number == 3

# Test setting an invalid position information (not a tuple/list of three values)
def test_set_invalid_position(base_object):
    with pytest.raises(AssertionError) as excinfo:
        base_object._set_ansible_position('invalid input')
    assert str(excinfo.value) == 'ansible_pos can only be set with a tuple/list of three values: source, line number, column number'

# Test setting an invalid position information (tuple/list but not of three elements)
def test_set_invalid_position_length(base_object):
    with pytest.raises(AssertionError) as excinfo:
        base_object._set_ansible_position(('source_code', 10))