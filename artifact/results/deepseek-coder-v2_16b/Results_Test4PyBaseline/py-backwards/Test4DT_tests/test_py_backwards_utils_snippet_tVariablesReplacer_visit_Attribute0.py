
# Module: py_backwards.utils.snippet
# test_variables_replacer.py
from typing import Dict
import ast
import pytest
from py_backwards.utils.snippet import VariablesReplacer

class Variable:
    def __init__(self, name: str, value: any):
        self.name = name
        self.value = value

# Helper function to create a dictionary of variables for testing
def create_variables_dict():
    return {
        'x': Variable('x', 10),
        'y': Variable('y', 20)
    }

# Test initialization with a dictionary of variables
def test_initialization_with_variables():
    variables = create_variables_dict()
    replacer = VariablesReplacer(variables)
    assert isinstance(replacer, VariablesReplacer)
    assert len(replacer._variables) == 2
    assert 'x' in replacer._variables and 'y' in replacer._variables

# Test replacing a field in an AST node
def test_visit_attribute():
    variables = create_variables_dict()
    replacer = VariablesReplacer(variables)
    
    class Node(ast.AST):
        _fields = ['value']

    # Create a sample AST node
    node = Node()
    node.value = 'original1'
    
    # Replace the field in the AST node
    replaced_node = replacer.visit_Attribute(node)  # Assuming `node` is an instance of ast.Attribute
    assert isinstance(replaced_node, Node)