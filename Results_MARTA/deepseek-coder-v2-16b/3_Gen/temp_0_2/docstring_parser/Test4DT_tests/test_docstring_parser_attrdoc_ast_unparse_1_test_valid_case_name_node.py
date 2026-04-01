
import ast
from docstring_parser.attrdoc import ast_unparse
import pytest

def test_valid_case_name_node():
    """Test conversion of a name AST node to source code."""
    name_node = ast.Name(id='x')
    result = ast_unparse(name_node)
    assert result == 'x'
