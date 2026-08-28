
import pytest
from py_backwards.utils.snippet import VariablesReplacer
from typing import Dict, TypeVar

T = TypeVar('T')

class Variable:
    def __init__(self, value):
        self.value = value



def test_replace_field_or_node_with_object():
    class MyClass:
        def __init__(self):
            self.var1 = None

    obj = MyClass()
    obj.var1 = 'originalVar'
    variables_dict = {'originalVar': 'uniqueVar'}
    replacer = VariablesReplacer(variables_dict)

    replaced_obj = replacer._replace_field_or_node(obj, 'var1', True)
    assert replaced_obj.var1 == 'uniqueVar', f"Expected 'uniqueVar', but got {replaced_obj.var1}"