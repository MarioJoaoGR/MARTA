
import pytest
from py_backwards.utils.snippet import VariablesReplacer
from typing import Dict, List

class Variable:
    def __init__(self, value):
        self.value = value

def test_invalid_initialization():
    with pytest.raises(TypeError):
        VariablesReplacer()

def test_valid_initialization():
    variables_dict = {'x': Variable(10), 'y': Variable(20)}
    replacer = VariablesReplacer(variables_dict)
    assert isinstance(replacer, VariablesReplacer)
    assert replacer._variables == variables_dict
