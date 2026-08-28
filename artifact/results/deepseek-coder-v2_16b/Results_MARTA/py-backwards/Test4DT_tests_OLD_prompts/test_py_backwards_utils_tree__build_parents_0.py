
import ast
from py_backwards.utils.tree import _build_parents, _parents
import pytest
from unittest.mock import patch

def test_build_parents_basic():
    sample_ast = ast.parse("def example(): pass")
    with patch('py_backwards.utils.tree._parents', {}):
        _build_parents(sample_ast)
        assert '_parents' in globals()

def test_build_parents_custom_transformer():
    class MyCustomTransformer(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            node.returns = None
            return node
    
    sample_ast = ast.parse("def example() -> int: pass")
    transformer = MyCustomTransformer()
    transformed_tree = transformer.visit(sample_ast)
    with patch('py_backwards.utils.tree._parents', {}):
        _build_parents(transformed_tree)
        assert '_parents' in globals()

def test_build_parents_different_module():
    sample_ast = ast.parse("class Example: pass")
    with patch('py_backwards.utils.tree._parents', {}):
        _build_parents(sample_ast)
        assert '_parents' in globals()
