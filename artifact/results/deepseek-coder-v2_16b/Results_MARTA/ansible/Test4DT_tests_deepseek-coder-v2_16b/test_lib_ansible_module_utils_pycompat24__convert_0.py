
import ast
import pytest
from tokenize import String

# Assuming _safe_names is defined somewhere above this call
_safe_names = {'x': 10, 'y': 20}

def test__convert_basic():
    """
    Test basic functionality of the _convert function.
    
    This includes converting constant nodes, tuple nodes, list nodes, dictionary nodes, name nodes, and unary negation nodes.
    """
    # Convert a constant node
    node = ast.parse("42").body[0].value
    converted_value = _convert(node)
    assert converted_value == 42
    
    # Convert a tuple node
    code = "def example(): return (1, 'two', 3.0)"
    tree = ast.parse(code)
    func_node = tree.body[0].body[0].value
    converted_tuple = _convert(func_node)
    assert converted_tuple == (1, 'two', 3.0)
    
    # Convert a list node
    code = "def example(): return [1, 'two', 3.0]"
    tree = ast.parse(code)
    func_node = tree.body[0].body[0].value
    converted_list = _convert(func_node)
    assert converted_list == [1, 'two', 3.0]
    
    # Convert a dictionary node
    code = "def example(): return {'a': 1, 'b': 2}"
    tree = ast.parse(code)
    func_node = tree.body[0].body[0].value
    converted_dict = _convert(func_node)
    assert converted_dict == {'a': 1, 'b': 2}
    
    # Convert a name node
    code = "x = 10"
    tree = ast.parse(code)
    name_node = tree.body[0].targets[0]
    converted_value = _convert(name_node)
    assert converted_value == 10
    
    # Convert a unary negation node
    code = "def example(): return -(1 + 2)"
    tree = ast.parse(code)
    func_node = tree.body[0].body[0].value
    converted_negation = _convert(func_node)
    assert converted_negation == -3
