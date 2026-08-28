
import pytest
from typing import Dict, Any
import ast
from py_backwards.utils.snippet import VariablesReplacer

# Helper class for the Variable used in the test cases
class Variable:
    def __init__(self, name: str, value: Any):
        self.name = name
        self.value = value

# Test case to ensure that replacing a field or node works correctly with string values
def test_replace_field_or_node_with_string():
    variables = {'original': 'new_var'}
    replacer = VariablesReplacer(variables)

    class Node(ast.AST):
        _fields = ['value']

    node = Node()
    node.value = ast.Name('original')
    replaced_node = replacer._replace_field_or_node(node, 'value', all_types=True)
    assert isinstance(replaced_node.value, ast.Name)