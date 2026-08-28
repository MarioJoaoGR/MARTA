
import pytest
from ansible.playbook.attribute import Attribute

# Test valid inputs
def test_valid_inputs():
    attr = Attribute(isa="int", default=10, required=True)
    assert attr.isa == "int"
    assert attr.default == 10
    assert attr.required is True

# Test edge cases for optional parameters
def test_edge_cases():
    attr = Attribute(isa="int", default=None, required=False)
    assert attr.isa == "int"
    assert attr.default is None
    assert attr.required is False

# Test invalid inputs that should raise TypeError
def test_invalid_inputs():
    with pytest.raises(TypeError):
        attr = Attribute(isa="list", listof="str", default=[1])
