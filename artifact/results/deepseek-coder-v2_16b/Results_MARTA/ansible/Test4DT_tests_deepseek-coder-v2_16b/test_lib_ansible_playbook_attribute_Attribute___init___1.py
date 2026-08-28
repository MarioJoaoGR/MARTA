
import pytest
from ansible.playbook.attribute import Attribute

# Test valid inputs for Attribute initialization
def test_valid_inputs():
    attr = Attribute(isa='int', default=10, required=True)
    assert attr.isa == 'int'
    assert attr.default == 10
    assert attr.required is True

# Test edge cases with None values and empty lists
def test_edge_cases():
    attr = Attribute(isa=None, default=None, required=False, listof='int')
    assert attr.isa is None
    assert attr.default is None
    assert not attr.required
    assert attr.listof == 'int'

# Test invalid inputs that should raise TypeError
def test_invalid_inputs():
    with pytest.raises(TypeError) as excinfo:
        attr = Attribute(isa='list', default=[1, 2])
    assert "defaults for FieldAttribute may not be mutable" in str(excinfo.value)
