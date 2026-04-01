
import ast
import inspect
import textwrap
import typing as T
import pytest
from docstring_parser.attrdoc import AttributeDocstrings

def test_invalid_input():
    visitor = AttributeDocstrings()
    
    # Test with invalid input type (int)
    with pytest.raises(TypeError):
        visitor.get_attr_docs(12345)
