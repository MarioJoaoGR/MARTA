
import pytest
from ansible.playbook.attribute import Attribute

# Test initialization with default values and basic type constraints
def test_default_initialization():
    attr = Attribute(isa='int', default=10, required=True)
    assert attr.isa == 'int'
    assert attr.default == 10
    assert attr.required is True

# Test initialization with string type and no default value
def test_string_type_no_default():
    attr = Attribute(isa='str', required=False)
    assert attr.isa == 'str'
    assert attr.default is None