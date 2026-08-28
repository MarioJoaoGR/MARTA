
import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.base import FieldAttributeBase


def test_invalid_attributes():
    field_base = FieldAttributeBase()
    invalid_attrs = frozenset({'attr3'})
    ds = {'attr1': 'value1', 'attr2': 'value2'}
    
    with pytest.raises(AnsibleParserError):
        field_base._validate_attributes(ds)