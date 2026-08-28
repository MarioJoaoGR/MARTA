
import pytest
from docstring_parser.numpydoc import ParamSection, DocstringParam






def test_no_optionality():
    param_section = ParamSection(title="Parameters", key="param")
    parsed_param = param_section._parse_item("threshold : float", "The threshold value for filtering.")
    assert parsed_param.arg_name == "threshold"
    assert parsed_param.type_name == "float"
    assert parsed_param.is_optional is False