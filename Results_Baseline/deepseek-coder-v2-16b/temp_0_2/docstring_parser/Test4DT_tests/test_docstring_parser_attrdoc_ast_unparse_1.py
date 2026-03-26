
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

# New test case to cover line 25: isinstance(node, ast.Constant)
def test_ast_unparse_constant_node():
    const_node = ast.Constant(value="test")
    assert ast_unparse(const_node) == "'test'"

# New test case to cover line 26: if isinstance(node, ast.Constant): return str(ast_get_constant_value(node))
def test_ast_unparse_constant_with_function():
    const_node = ast.Constant(value=42)
    assert ast_unparse(const_node) == "42"  # This is already covered by the existing test, but adding for clarity

# New test case to cover line 27: if isinstance(node, ast.Name): return node.id
def test_ast_unparse_name_node():
    name_node = ast.Name(id='y', ctx='load')
    assert ast_unparse(name_node) == "y"

# New test case to cover line 29: return None
def test_ast_unparse_none():
    none_node = ast.Constant(value=None)