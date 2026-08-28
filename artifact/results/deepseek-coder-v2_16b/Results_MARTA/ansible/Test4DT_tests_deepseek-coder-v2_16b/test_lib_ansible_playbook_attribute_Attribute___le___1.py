
import pytest
from ansible.playbook.attribute import Attribute

def test_valid_inputs():
    attr = Attribute(isa="int", default=10, required=True)
    assert attr.isa == "int"
    assert attr.default == 10
    assert attr.required is True

def test_edge_cases():
    attr = Attribute(isa=None, private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)
    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate is False
    assert attr.inherit is True
    assert attr.alias is None

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Attribute(isa="int", default=[1, 2])
