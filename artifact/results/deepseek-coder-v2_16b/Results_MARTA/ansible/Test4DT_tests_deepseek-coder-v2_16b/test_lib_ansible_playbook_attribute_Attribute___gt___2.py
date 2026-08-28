
import pytest
from ansible.playbook.attribute import Attribute

# Test valid inputs
def test_valid_inputs():
    attr = Attribute(isa='int', default=10, required=True)
    assert attr.isa == 'int'
    assert attr.default == 10
    assert attr.required is True

# Test edge cases
def test_edge_cases():
    attr_none = Attribute(isa=None, default=None, required=False)
    assert attr_none.isa is None
    assert attr_none.default is None
    assert not attr_none.required
    
    attr_list = Attribute(isa='list', listof=None)
    assert attr_list.isa == 'list'
    assert attr_list.listof is None

# Test invalid inputs and error handling
def test_invalid_inputs():
    with pytest.raises(TypeError):
        attr = Attribute(default=10, isa='int')
