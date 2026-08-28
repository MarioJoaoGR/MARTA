
import pytest
from docstring_parser.numpydoc import ParamSection, DocstringParam







def test_no_default_value():
    param_section = ParamSection(title="Parameters", key="param")
    parsed_param = param_section._parse_item("config_path : str, optional", "Path to the configuration file.")
    assert parsed_param.default is None