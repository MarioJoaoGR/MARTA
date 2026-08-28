
import pytest
from ansible.playbook.base import FieldAttributeBase, AnsibleParserError
from unittest.mock import patch


def test_load_vars_with_dict():
    field_attribute = FieldAttributeBase()
    variables_dict = {'var1': 'value1', 'var2': 'value2'}
    with patch('ansible.playbook.base.combine_vars') as mock_combine_vars:
        mock_combine_vars.return_value = variables_dict  # Mock the return value of combine_vars
        result = field_attribute._load_vars('example_attr', variables_dict)
        assert result == variables_dict

def test_load_vars_with_list():
    field_attribute = FieldAttributeBase()
    variables_list = [{'var3': 'value3'}, {'var4': 'value4'}]
    with patch('ansible.playbook.base.combine_vars') as mock_combine_vars:
        mock_combine_vars.return_value = {'var3': 'value3', 'var4': 'value4'}  # Mock the return value of combine_vars
        result = field_attribute._load_vars('example_attr', variables_list)
        assert result == {'var3': 'value3', 'var4': 'value4'}

def test_load_vars_invalid_specification():
    field_attribute = FieldAttributeBase()
    with pytest.raises(AnsibleParserError):
        field_attribute._load_vars('example_attr', 'invalid_specification')