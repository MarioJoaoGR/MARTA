
import ast
from typing import Any as T
from docstring_parser.attrdoc import ast_get_constant_value
import pytest

def test_valid_input():
    class ConstantNode(ast.AST):
        value = 42

    const_node = ConstantNode()
    assert ast_get_constant_value(const_node) == 42
