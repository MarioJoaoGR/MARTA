
import pytest
from py_backwards.utils.snippet import VariablesReplacer
from typing import Dict, Union

class Variable:
    def __init__(self, value):
        self.value = value

def test_valid_input_dictionary():
    variables_dict = {'x': Variable(10), 'y': Variable(20)}
    replacer = VariablesReplacer(variables_dict)
    
    class TestNode:
        def __init__(self):
            self.field = None

    node = TestNode()
    assert isinstance(replacer._replace_field_or_node(node, 'field'), TestNode)

