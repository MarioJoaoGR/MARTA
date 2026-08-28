
import pytest
from ansible.playbook.attribute import Attribute

# Test valid case 1
def test_valid_case_1():
    attr = Attribute(isa="int", default=10, required=True)
    assert attr.isa == "int"
    assert attr.default == 10
    assert attr.required is True

# Test edge case 2
def test_edge_case_2():
    attr = Attribute(isa=None, private=False, default=None, required=False, listof=[], priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)
    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof == []
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate is False
    assert attr.inherit is True
    assert attr.alias is None

# Test invalid case 3
def test_invalid_case_3():
    with pytest.raises(TypeError) as excinfo:
        Attribute(isa="list", default=[1, 2], required=True)
    assert str(excinfo.value) == "defaults for FieldAttribute may not be mutable, please provide a callable instead"
