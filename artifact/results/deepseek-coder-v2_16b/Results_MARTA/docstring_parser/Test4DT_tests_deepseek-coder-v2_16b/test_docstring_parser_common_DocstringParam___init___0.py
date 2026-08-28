
import pytest
from docstring_parser.common import DocstringParam

def test_valid_init():
    """Test that a valid instance of DocstringParam can be created."""
    param = DocstringParam(args=['name'], description='Name of the entity', arg_name='name', type_name='str', is_optional=False, default=None)
    assert isinstance(param, DocstringParam)
    assert param.arg_name == 'name'
    assert param.type_name == 'str'
    assert param.is_optional is False
    assert param.default is None

def test_valid_init_with_optional():
    """Test that a valid instance of DocstringParam can be created with an optional argument."""
    param = DocstringParam(args=['age'], description='Age of the entity', arg_name='age', type_name='int', is_optional=True, default='18')
    assert isinstance(param, DocstringParam)
    assert param.arg_name == 'age'
    assert param.type_name == 'int'
    assert param.is_optional is True
    assert param.default == '18'

def test_valid_init_without_default():
    """Test that a valid instance of DocstringParam can be created without a default value."""
    param = DocstringParam(args=['is_active'], description='Indicates whether the entity is active', arg_name='is_active', type_name=None, is_optional=False, default=True)
    assert isinstance(param, DocstringParam)
    assert param.arg_name == 'is_active'
    assert param.type_name is None
    assert param.is_optional is False
    assert param.default == True

def test_invalid_inputs():
    """Test that an exception is raised for invalid inputs."""
    with pytest.raises(Exception):
        DocstringParam()  # Missing required arguments
