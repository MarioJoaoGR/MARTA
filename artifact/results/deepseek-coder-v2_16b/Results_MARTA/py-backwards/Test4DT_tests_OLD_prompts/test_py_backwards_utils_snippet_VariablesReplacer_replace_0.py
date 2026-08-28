
import pytest
import ast
from py_backwards.utils.snippet import VariablesReplacer, Variable

# Test replacing variables in a dictionary

# Test replacing variables in an AST

# Test using the replace method with a tree structure
def test_replace_method_with_ast():
    class Variable:
        def __init__(self, value):
            self.value = value
    
    variables_dict = {
        'x': Variable(10),
        'y': Variable(20)
    }
    
    with pytest.raises(TypeError):
        modified_tree = VariablesReplacer.replace(cls=VariablesReplacer, tree=ast.parse("def example_function(): x = 10; y = x + 5"), variables=variables_dict)