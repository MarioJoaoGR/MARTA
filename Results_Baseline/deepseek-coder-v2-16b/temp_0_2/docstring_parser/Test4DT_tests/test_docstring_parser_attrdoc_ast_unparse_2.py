
import ast
from typing import Optional as T

# Import the function from its module
from docstring_parser.attrdoc import ast_unparse

def test_ast_unparse_constant():
    const_node = ast.Constant(value=42)
    assert ast_unparse(const_node) == "42"

def test_ast_unparse_name():
    name_node = ast.Name(id='x', ctx='load')
    assert ast_unparse(name_node) == "x"

# New test cases for the uncovered lines 25-29
def test_ast_unparse_none():
    none_node = None