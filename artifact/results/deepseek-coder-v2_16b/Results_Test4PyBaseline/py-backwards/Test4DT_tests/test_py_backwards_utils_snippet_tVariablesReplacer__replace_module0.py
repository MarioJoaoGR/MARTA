
import pytest
from typing import Dict, Any
from py_backwards.utils.snippet import VariablesReplacer

# Fixture to create a sample Variable class instance
@pytest.fixture
def variable():
    return Variable('x', 10)

# Fixture to create a sample VariablesReplacer instance with variables dictionary
@pytest.fixture
def replacer(variable):
    variables_dict = {'x': variable, 'y': Variable('y', 20)}
    return VariablesReplacer(variables_dict)

class Variable:
    def __init__(self, name: str, value: Any):
        self.name = name
        self.value = value

# Test case for initializing the VariablesReplacer with a dictionary of variables
def test_initialization():
    variable1 = Variable('x', 10)
    variable2 = Variable('y', 20)
    variables_dict = {'x': variable1, 'y': variable2}
    
    replacer = VariablesReplacer(variables_dict)
    assert isinstance(replacer._variables['x'], Variable)
    assert isinstance(replacer._variables['y'], Variable)
    assert replacer._variables['x'].name == 'x'
    assert replacer._variables['y'].name == 'y'

# Test case for replacing a field in an AST node with a variable name that exists in _variables
def test_replace_module_with_existing_variable(replacer):
    module = "a.b.x"
    replaced_module = replacer._replace_module(module)