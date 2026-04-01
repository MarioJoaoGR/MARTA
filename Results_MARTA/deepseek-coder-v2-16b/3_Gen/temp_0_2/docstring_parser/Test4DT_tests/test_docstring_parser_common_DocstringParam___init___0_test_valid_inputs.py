
import pytest
from docstring_parser.common import DocstringParam

def test_valid_inputs():
    # Test valid inputs for the DocstringParam class
    param = DocstringParam(
        args=["arg1", "arg2"],
        description="This is an argument used for...",
        arg_name="argName",
        type_name="int",
        is_optional=True,
        default="default_value"
    )
    
    assert param.args == ["arg1", "arg2"]
    assert param.description == "This is an argument used for..."
    assert param.arg_name == "argName"
    assert param.type_name == "int"
    assert param.is_optional is True
    assert param.default == "default_value"
