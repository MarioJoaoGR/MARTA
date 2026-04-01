
import ast
import inspect
import textwrap
import typing as T
import pytest
from docstring_parser.attrdoc import AttributeDocstrings

def test_invalid_input():
    visitor = AttributeDocstrings()
    
    # Test with an invalid type (int) to see if it raises appropriate errors
    with pytest.raises(TypeError):
        visitor.get_attr_docs(12345)
