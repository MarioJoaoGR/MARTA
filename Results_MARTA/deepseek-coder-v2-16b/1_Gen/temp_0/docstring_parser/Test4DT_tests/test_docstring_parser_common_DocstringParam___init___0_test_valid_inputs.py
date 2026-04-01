
import pytest
from docstring_parser.common import DocstringParam

def test_valid_inputs():
    param = DocstringParam(
        args=["param1", "param2"],
        description="First and second parameters",
        arg_name="example_arg",
        type_name="int",
        is_optional=False,
        default="None"
    )
    
    assert param.args == ["param1", "param2"]
    assert param.description == "First and second parameters"
    assert param.arg_name == "example_arg"
    assert param.type_name == "int"
    assert param.is_optional is False
    assert param.default == "None"
