
import pytest
from docstring_parser.numpydoc import ParamSection, DocstringParam





def test_type_no_optionality():
    param_section = ParamSection(title="Parameters", key="param")
    parsed_param = param_section._parse_item("count : int", "The count of items.")
    assert parsed_param.arg_name == "count"
    assert parsed_param.type_name == "int"
    assert parsed_param.is_optional is False
    assert parsed_param.default is None


def test_boolean_parameter():
    param_section = ParamSection(title="Parameters", key="param")
    parsed_param = param_section._parse_item("debug : bool, optional", "Enable debug mode.")
    assert parsed_param.arg_name == "debug"
    assert parsed_param.type_name == "bool"
    assert parsed_param.is_optional is True
    assert parsed_param.default is None