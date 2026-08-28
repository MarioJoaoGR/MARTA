
import pytest
from docstring_parser.common import DocstringParam

def test_invalid_inputs():
    """Test that the DocstringParam raises an exception for invalid inputs."""
    with pytest.raises(Exception):
        # Test case where args is not a list
        param = DocstringParam(args="not_a_list", description='Description', arg_name='arg_name', type_name=None, is_optional=False, default=None)
        
        # Test case where arg_name is missing
        param = DocstringParam(args=['arg'], description='Description', type_name=None, is_optional=False, default=None)
        
        # Test case where is_optional is not a bool
        param = DocstringParam(args=['arg'], description='Description', arg_name='arg_name', type_name=None, is_optional="not_a_bool", default=None)
        
        # This should raise an exception due to invalid input types
