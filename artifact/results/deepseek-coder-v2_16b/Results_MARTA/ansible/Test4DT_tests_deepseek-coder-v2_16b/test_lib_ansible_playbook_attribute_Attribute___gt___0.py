
import pytest
from ansible.playbook.attribute import Attribute

# Test valid inputs for Attribute class with valid parameters
def test_valid_inputs():
    attr = Attribute(isa='int', default=10, required=True)
    assert attr.isa == 'int'
    assert attr.default == 10
    assert attr.required is True

# Test edge cases for Attribute class with boundary values and None inputs
def test_edge_cases():
    attr_none = Attribute()
    assert attr_none.isa is None
    assert attr_none.default is None
    assert not attr_none.required

    attr_empty = Attribute(isa='int', default=[], required=False)
    assert attr_empty.isa == 'int'
    assert attr_empty.default == []
    assert not attr_empty.required

# Test invalid inputs for Attribute class to raise TypeError when default is not callable
def test_invalid_inputs():
    with pytest.raises(TypeError) as e:
        Attribute(isa='list', listof='str', default=[])
    assert str(e.value) == 'defaults for FieldAttribute may not be mutable, please provide a callable instead'
