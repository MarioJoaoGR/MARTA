
import ast
from docstring_parser.attrdoc import ast_unparse
import typing as T
import pytest

def test_valid_case_constant_node():
    const_node = ast.Constant(value=42)
    result = ast_unparse(const_node)
    assert result == "42"
