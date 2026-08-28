
import ast
from py_backwards.utils.tree import get_non_exp_parent_and_index
import pytest
from unittest.mock import patch

def test_valid_case_function_definition():
    sample_ast = ast.parse("def example(): pass")
    with patch('py_backwards.utils.tree.get_parent', return_value=sample_ast):
        parent_node, index = get_non_exp_parent_and_index(sample_ast, sample_ast.body[0])
        assert isinstance(parent_node, ast.Module)
        assert index == 0

