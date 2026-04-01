
import ast
import inspect
import textwrap
import typing as T
import pytest
from docstring_parser.attrdoc import AttributeDocstrings

def test_invalid_input():
    visitor = AttributeDocstrings()
    with pytest.raises(TypeError):
        # Passing an integer instead of a class or module should raise TypeError
        visitor.get_attr_docs(12345)
