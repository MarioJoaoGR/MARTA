
import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleAssertionError

def test_deserialize_with_none():
    field_attribute = FieldAttributeBase()
    with pytest.raises(AnsibleAssertionError) as excinfo:
        field_attribute.deserialize(None)
    assert str(excinfo.value) == 'data (None) should be a dict but is a <class \'NoneType\'>'

def test_deserialize_with_invalid_type():
    field_attribute = FieldAttributeBase()
    with pytest.raises(AnsibleAssertionError) as excinfo:
        field_attribute.deserialize("not a dictionary")
    assert str(excinfo.value) == 'data (not a dictionary) should be a dict but is a <class \'str\'>'
