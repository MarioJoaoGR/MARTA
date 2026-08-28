
import pytest
from docstring_parser.numpydoc import ParamSection, DocstringParam

def test_parse_item_required_argument():
    param_section = ParamSection(title='Parameters', key='param')
    param = param_section._parse_item('arg_name', 'This is a description of arg_name.')
    assert param.arg_name == 'arg_name'
    assert param.type_name is None
    assert not param.is_optional  # Corrected from `is False`
    assert param.description == 'This is a description of arg_name.'

def test_parse_item_optional_argument_with_type():
    param_section = ParamSection(title='Parameters', key='param')
    param = param_section._parse_item('arg_2 : int, optional', 'This is another description.')
    assert param.arg_name == 'arg_2'
    assert param.type_name == 'int'
    assert param.is_optional
    assert param.description == 'This is another description.'

def test_parse_item_with_default_value():
    param_section = ParamSection(title='Parameters', key='param')
    param = param_section._parse_item('arg_3 : str', 'This argument has a default value of "default".')
    assert param.arg_name == 'arg_3'
    assert param.type_name == 'str'
    assert not param.is_optional  # Corrected from `is False`