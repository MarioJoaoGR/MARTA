
import pytest
from docstring_parser.common import DocstringParam

def test_edge_cases():
    # Test with None values
    param1 = DocstringParam(args=None, description=None, arg_name='', type_name=None, is_optional=True, default=None)
    assert param1.arg_name == ''
    assert param1.type_name is None
    assert param1.is_optional is True
    assert param1.default is None

    # Test with empty lists
    param2 = DocstringParam(args=[], description=None, arg_name='example_arg', type_name="int", is_optional=False, default="None")
    assert param2.args == []
    assert param2.description is None
    assert param2.arg_name == 'example_arg'
    assert param2.type_name == "int"
    assert not param2.is_optional
    assert param2.default == "None"

    # Test with boundary values
    param3 = DocstringParam(args=['param1'], description='First parameter', arg_name='param1', type_name=None, is_optional=True, default=None)
    assert param3.args == ['param1']
    assert param3.description == 'First parameter'
    assert param3.arg_name == 'param1'
    assert param3.type_name is None
    assert param3.is_optional is True
    assert param3.default is None
