
import pytest
from ansible.playbook.attribute import Attribute

# Scenario 1: Test valid inputs
def test_valid_inputs():
    attr = Attribute(isa="int", default=10, required=True)
    assert attr.isa == "int"
    assert attr.default == 10
    assert attr.required is True

# Scenario 2: Test edge cases
def test_edge_cases():
    attr = Attribute(isa=None, default=None, required=False)
    assert attr.isa is None
    assert attr.default is None
    assert attr.required is False

# Scenario 3: Test invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        attr = Attribute(isa="list", default=[1, 2])
