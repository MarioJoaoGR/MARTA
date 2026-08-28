
import pytest
from typing import Dict, Any
import ast
from py_backwards.utils.snippet import VariablesReplacer

class Variable:
    def __init__(self, name: str, value: Any):
        self.name = name
        self.value = value

# Define a dictionary of variables
variables_dict = {
    'x': Variable('x', 10),
    'y': Variable('y', 20)
}

# Initialize the VariablesReplacer with the variables dictionary
replacer = VariablesReplacer(variables_dict)

def test_initialization():
    assert isinstance(replacer, VariablesReplacer)
    assert replacer._variables == variables_dict

def test_replace_field_or_node_with_existing_name():
    node = ast.ExceptHandler()
    node.name = 'x'
    replaced_node = replacer._replace_field_or_node(node, 'name')