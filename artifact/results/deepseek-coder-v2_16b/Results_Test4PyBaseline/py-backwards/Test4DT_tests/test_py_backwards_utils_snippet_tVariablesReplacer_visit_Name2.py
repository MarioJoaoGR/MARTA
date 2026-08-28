
import pytest
from typing import Dict, Any
import ast
from py_backwards.utils.snippet import VariablesReplacer

# Helper class for the Variable used in the test cases
class Variable:
    def __init__(self, name: str, value: Any):
        self.name = name
        self.value = value

# Test case for replacing a field or node in an AST using VariablesReplacer
def test_replace_field_or_node():
    variables = {'original1': 'new_var1', 'original2': Variable('original2', None)}
    replacer = VariablesReplacer(variables)

    class Node(ast.AST):
        _fields = ['value']

    # Test replacing a field with an existing variable name
    node = Node()
    node.value = ast.Name('original1')
    replaced_node = replacer._replace_field_or_node(node, 'value', all_types=True)
    assert isinstance(replaced_node.value, ast.Name)