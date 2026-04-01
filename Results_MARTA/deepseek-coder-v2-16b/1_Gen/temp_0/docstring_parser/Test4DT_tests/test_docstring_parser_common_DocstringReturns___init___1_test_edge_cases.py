
import pytest
from typing import List, Optional
from docstring_parser.common import DocstringReturns

def test_edge_cases():
    # Test initialization with edge cases
    docstring_meta = DocstringReturns(args=["arg1", "arg2"], description="This function does something.", type_name="int", is_generator=False, return_name="result")
    
    assert docstring_meta.args == ["arg1", "arg2"]
    assert docstring_meta.description == "This function does something."
    assert docstring_meta.type_name == "int"
    assert not docstring_meta.is_generator
    assert docstring_meta.return_name == "result"
