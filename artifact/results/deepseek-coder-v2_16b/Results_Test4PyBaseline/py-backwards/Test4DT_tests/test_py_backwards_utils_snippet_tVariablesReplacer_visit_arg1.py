
# Module: py_backwards.utils.snippet
from py_backwards.utils.snippet import VariablesReplacer
import ast
import pytest
from typing import Any  # Importing the missing 'Any' type from the standard library

# Define a sample Variable class for testing purposes.
class Variable:
    def __init__(self, name: str, value: Any):
        self.name = name
        self.value = value

# Test cases for VariablesReplacer class
def test_initialization():
    variables_dict = {
        'x': Variable('x', 10),
        'y': Variable('y', 20)
    }
    replacer = VariablesReplacer(variables_dict)
    assert isinstance(replacer, VariablesReplacer), "Initialization should create an instance of VariablesReplacer"

def test_replace_field_or_node():
    variables_dict = {
        'original1': 'new_var1',
        'original2': Variable('original2', None)
    }
    replacer = VariablesReplacer(variables_dict)
    
    class Node(ast.AST):
        _fields = ['value']
    
    node = Node()
    node.value = 'original1'
    replaced_node = replacer._replace_field_or_node(node, 'value', all_types=True)
    assert replaced_node.value == 'new_var1', "Field should be replaced with the new variable name"
    
    node2 = Node('original2')
    replaced_node2 = replacer._replace_field_or_node(node2, 'value', all_types=False)
    assert replaced_node2.value == 'original2', "Field should be replaced with the new variable name"

# Additional test cases for visit_arg method in VariablesReplacer class
def test_visit_arg():
    variables_dict = {
        'x': Variable('x', 10),
        'y': Variable('y', 20)
    }
    replacer = VariablesReplacer(variables_dict)
    
    # Create a sample ast.arg node for testing
    arg_node = ast.arg(name='test_arg')
    
    # Test replacing the 'arg' field of the ast.arg node
    replaced_arg_node = replacer.visit_arg(arg_node)
    assert isinstance(replaced_arg_node, ast.arg), "visit_arg should return an instance of ast.arg"