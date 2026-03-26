
import ast
import pytest
from typing import Optional

# Import the function from its module
from docstring_parser.attrdoc import ast_unparse

def test_ast_unparse_constant():
    constant_node = ast.Constant(value=42)
    assert ast_unparse(constant_node) == '42'

def test_ast_unparse_name():
    name_node = ast.Name(id='x')
    assert ast_unparse(name_node) == 'x'

def test_ast_unparse_unsupported_node():
    class UnsupportedNode(ast.AST): pass
    unsupported_node = UnsupportedNode()