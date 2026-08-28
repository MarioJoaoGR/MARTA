
import ast
import pytest
from py_backwards.utils.tree import get_non_exp_parent_and_index, get_parent




def test_complex_ast_with_multiple_methods():
    sample_ast = ast.parse("""
class ComplexExample:
    def method1(self):
        pass
    def method2(self):
        pass
""")
    for node in sample_ast.body:
        if isinstance(node, ast.FunctionDef):
            parent_node, index = get_non_exp_parent_and_index(sample_ast, node)
            assert isinstance(parent_node, ast.ClassDef)
            assert index >= 0 and index < len(sample_ast.body)