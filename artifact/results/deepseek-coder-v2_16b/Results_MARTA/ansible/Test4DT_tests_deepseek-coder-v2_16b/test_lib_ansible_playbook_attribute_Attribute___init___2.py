
import pytest
from ansible.playbook.attribute import Attribute

# Test scenario 1: Creating an Attribute instance without providing a default value when isa is not None
def test_init_without_default():
    attr = Attribute(isa="int", required=True)
    assert attr.isa == "int"
    assert attr.required is True
    assert attr.default is None

# Test scenario 2: Creating an Attribute instance with a default value when isa is not callable
def test_init_with_callable_default():
    with pytest.raises(TypeError):
        attr = Attribute(isa="list", default=[], required=True)
