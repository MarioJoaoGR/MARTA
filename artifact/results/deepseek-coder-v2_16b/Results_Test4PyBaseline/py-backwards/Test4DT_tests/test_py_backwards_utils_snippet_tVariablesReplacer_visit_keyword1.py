
# Module: py_backwards.utils.snippet
from py_backwards.utils.snippet import VariablesReplacer
import ast
from typing import Dict, Any

class Variable:
    def __init__(self, name: str, value: Any):
        self.name = name
        self.value = value

# Test case for initializing the VariablesReplacer class with a dictionary of variables.
def test_variablesreplacer_initialization():
    variables_dict = {
        'x': Variable('x', 10),
        'y': Variable('y', 20)
    }
    replacer = VariablesReplacer(variables_dict)
    assert isinstance(replacer, VariablesReplacer), "The object should be an instance of VariablesReplacer"
    assert len(replacer._variables) == 2, "The number of variables should match the input dictionary"
    assert 'x' in replacer._variables and 'y' in replacer._variables, "Both keys from the dictionary should be present"

# Test case for replacing fields in an AST node.
def test_replace_field_or_node():
    variables_dict = {
        'original1': Variable('new_var1', None),
        'original2': Variable('new_var2', None)
    }
    replacer = VariablesReplacer(variables_dict)
    
    class Node(ast.AST):
        _fields = ['value']
    
    node = Node()
    node.value = 'original1'
    replaced_node = replacer._replace_field_or_node(node, 'value', all_types=True)