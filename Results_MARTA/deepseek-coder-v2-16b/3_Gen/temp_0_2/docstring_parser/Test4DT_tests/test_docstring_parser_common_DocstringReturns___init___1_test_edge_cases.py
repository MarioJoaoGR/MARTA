
import pytest
from docstring_parser.common import DocstringReturns

def test_edge_cases():
    # Test with None and empty lists for args, description, type_name, is_generator, return_name
    
    # Test with None for all parameters
    docstring = DocstringReturns(args=None, description=None, type_name=None, is_generator=True)
    assert docstring.args is None
    assert docstring.description is None
    assert docstring.type_name is None
    assert docstring.is_generator is True
    assert docstring.return_name is None
    
    # Test with empty list for args
    docstring = DocstringReturns(args=[], description="This function does something.", type_name="int", is_generator=False, return_name="result")
    assert docstring.args == []
    assert docstring.description == "This function does something."
    assert docstring.type_name == "int"
    assert docstring.is_generator is False
    assert docstring.return_name == "result"
    
    # Test with None for description, type_name, and return_name
    docstring = DocstringReturns(args=["arg1", "arg2"], description=None, type_name=None, is_generator=True)
    assert docstring.args == ["arg1", "arg2"]
    assert docstring.description is None
    assert docstring.type_name is None
    assert docstring.is_generator is True
    assert docstring.return_name is None
    
    # Test with empty list for args and None for other parameters
    docstring = DocstringReturns(args=[], description=None, type_name=None, is_generator=True, return_name=None)
    assert docstring.args == []
    assert docstring.description is None
    assert docstring.type_name is None
    assert docstring.is_generator is True
    assert docstring.return_name is None
    
    # Test with all parameters set to default values
    docstring = DocstringReturns(args=["arg1", "arg2"], description="This function does something.", type_name="int", is_generator=False, return_name="result")
    assert docstring.args == ["arg1", "arg2"]
    assert docstring.description == "This function does something."
    assert docstring.type_name == "int"
    assert docstring.is_generator is False
    assert docstring.return_name == "result"
