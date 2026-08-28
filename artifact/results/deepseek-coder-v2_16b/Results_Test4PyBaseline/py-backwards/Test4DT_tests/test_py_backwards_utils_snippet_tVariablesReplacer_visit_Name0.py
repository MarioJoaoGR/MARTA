
import pytest
from typing import Dict, Any
import ast
from py_backwards.utils.snippet import VariablesReplacer

# Helper class for the Variable used in the test cases
class Variable:
    def __init__(self, name: str, value: Any):
        self.name = name
        self.value = value

# Test case for initializing VariablesReplacer with a dictionary of variables
def test_initialization():
    variables_dict = {
        'x': Variable('x', 10),
        'y': Variable('y', 20)
    }
    replacer = VariablesReplacer(variables_dict)
    assert isinstance(replacer, VariablesReplacer)
    assert len(replacer._variables) == 2
    assert replacer._variables['x'].name == 'x'
    assert replacer._variables['y'].name == 'y'

# Test case for replacing a field or node in an AST using VariablesReplacer
def test_replace_field_or_node():
    variables = {'original1': 'new_var1', 'original2': Variable('original2', None)}
    replacer = VariablesReplacer(variables)

    class Node(ast.AST):
        _fields = ['value']

    node = Node()
    node.value = ast.Name('original1')
    replaced_node = replacer._replace_field_or_node(node, 'value', all_types=True)
    assert isinstance(replaced_node.value, ast.Name)