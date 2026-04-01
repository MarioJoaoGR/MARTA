
import pytest
from docstring_parser.common import DocstringParam

def test_valid_inputs():
    # Test initializing a DocstringParam instance with valid inputs
    param = DocstringParam(
        args=['example_arg'],
        description='This is an example parameter.',
        arg_name='example_arg',
        type_name='int',
        is_optional=False,
        default=None
    )
    
    assert isinstance(param, DocstringParam)
    assert param.args == ['example_arg']
    assert param.description == 'This is an example parameter.'
    assert param.arg_name == 'example_arg'
    assert param.type_name == 'int'
    assert param.is_optional == False
    assert param.default == None
