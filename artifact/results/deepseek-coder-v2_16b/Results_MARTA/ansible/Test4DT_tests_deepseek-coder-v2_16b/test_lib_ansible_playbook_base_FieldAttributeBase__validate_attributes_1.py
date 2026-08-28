
import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError

# Test 1: Valid attributes validation
def test_valid_attributes_validation():
    field_base = FieldAttributeBase()
    ds = {'attr1': 'value1', 'attr2': 'value2'}
    field_base._valid_attrs = {'attr1': None, 'attr2': None}
    
    # No error should be raised
    field_base._validate_attributes(ds)

# Test 2: Invalid attributes validation
def test_invalid_attributes_validation():
    field_base = FieldAttributeBase()
    ds = {'invalid_attr': 'value'}
    field_base._valid_attrs = {'attr1': None, 'attr2': None}
    
    with pytest.raises(AnsibleParserError):
        field_base._validate_attributes(ds)

# Test 3: Missing lines validation
def test_missing_lines_validation():
    field_base = FieldAttributeBase()
    ds = {'attr1': 'value1'}
    field_base._valid_attrs = {'attr2': None}
    
    with pytest.raises(AnsibleParserError):
        field_base._validate_attributes(ds)
