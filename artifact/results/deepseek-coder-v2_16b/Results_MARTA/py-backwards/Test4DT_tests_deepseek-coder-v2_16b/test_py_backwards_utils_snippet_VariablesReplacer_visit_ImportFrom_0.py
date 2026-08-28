
import pytest
from typing import Dict
import ast
from py_backwards.utils.snippet import VariablesReplacer, Variable

# Test 1: Initialization with Variables Dictionary
def test_initialization_with_variables():
    class Variable:
        def __init__(self, value):
            self.value = value

    variables_dict = {
        'x': Variable(10),
        'y': Variable(20)
    }

    replacer = VariablesReplacer(variables_dict)
    assert hasattr(replacer, '_variables') and isinstance(replacer._variables, Dict)
    assert len(replacer._variables) == 2
    assert replacer._variables['x'].value == 10
    assert replacer._variables['y'].value == 20

# Test 2: Replace Variables with Unique Names

# Test 3: Replace Module Name in ImportFrom Node
def test_replace_module_name():
    variables_dict = {
        'math': 'uniqueModuleName'
    }

    replacer = VariablesReplacer(variables_dict)
    import_node = ast.parse("from math import sqrt").body[0]
    modified_node = replacer.visit_ImportFrom(import_node)
    
    assert modified_node.module == 'uniqueModuleName'

# Test 4: Replace Module Name in ImportFrom Node with Non-Existent Module

# Test 5: Replace Module Name in ImportFrom Node with Empty String
def test_replace_empty_module_name():
    variables_dict = {
        'math': ''
    }

    replacer = VariablesReplacer(variables_dict)
    import_node = ast.parse("from math import sqrt").body[0]
    modified_node = replacer.visit_ImportFrom(import_node)
    
    assert modified_node.module == ''