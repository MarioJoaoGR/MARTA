
import pytest
from py_backwards.utils.helpers import VariablesGenerator

# Test case for generating a unique name with a new variable
def test_generate_new_variable():
    # First call should generate _py_backwards_var_0
    assert VariablesGenerator.generate('var') == '_py_backwards_var_0'
    
    # Second call should generate _py_backwards_another_var_1