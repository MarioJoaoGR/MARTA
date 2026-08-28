
# Module: ansible.playbook.attribute
# test_attribute.py
from ansible.playbook.attribute import Attribute, _CONTAINERS
import pytest

def test_init_with_mutable_default():
    with pytest.raises(TypeError) as excinfo:
        Attribute(isa='list', default=[1, 2, 3])
    assert str(excinfo.value) == 'defaults for FieldAttribute may not be mutable, please provide a callable instead'

def test_init_with_mutable_default_dict():
    with pytest.raises(TypeError) as excinfo:
        Attribute(isa='dict', default={'key': 'value'})