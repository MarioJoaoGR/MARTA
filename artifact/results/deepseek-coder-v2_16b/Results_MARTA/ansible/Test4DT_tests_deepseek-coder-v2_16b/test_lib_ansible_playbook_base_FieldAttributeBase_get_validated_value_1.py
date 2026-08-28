
import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.playbook.attribute import Attribute

def test_get_validated_value_string():
    field_base = FieldAttributeBase()
    attribute = Attribute(isa='str')
    validated_value = field_base.get_validated_value('example', attribute, 'Hello, World!', None)
    assert isinstance(validated_value, str), f"Expected a string but got {type(validated_value)}"

def test_get_validated_value_int():
    field_base = FieldAttributeBase()
    attribute = Attribute(isa='int')
    validated_value = field_base.get_validated_value('example', attribute, '123', None)
    assert isinstance(validated_value, int), f"Expected an integer but got {type(validated_value)}"

def test_get_validated_value_float():
    field_base = FieldAttributeBase()
    attribute = Attribute(isa='float')
    validated_value = field_base.get_validated_value('example', attribute, '123.45', None)
    assert isinstance(validated_value, float), f"Expected a float but got {type(validated_value)}"

def test_get_validated_value_bool():
    field_base = FieldAttributeBase()
    attribute = Attribute(isa='bool')
    validated_value = field_base.get_validated_value('example', attribute, 'True', None)
    assert isinstance(validated_value, bool), f"Expected a boolean but got {type(validated_value)}"

def test_get_validated_value_percent():
    field_base = FieldAttributeBase()
    attribute = Attribute(isa='percent')
    validated_value = field_base.get_validated_value('example', attribute, '75%', None)
    assert isinstance(validated_value, float), f"Expected a percent but got {type(validated_value)}"


def test_get_validated_value_dict():
    field_base = FieldAttributeBase()
    attribute = Attribute(isa='dict')
    validated_value = field_base.get_validated_value('example', attribute, {'key1': 'value1', 'key2': 'value2'}, None)
    assert isinstance(validated_value, dict), f"Expected a dictionary but got {type(validated_value)}"
