
# Module: py_backwards.utils.snippet
# test_variablesreplacer.py
from typing import Dict, Union
import pytest
import ast
from py_backwards.utils.snippet import VariablesReplacer

class Variable:
    def __init__(self, unique_name: str):
        self.unique_name = unique_name

    def get_name(self) -> str:
        return self.unique_name

@pytest.fixture
def variables():
    return {
        'old_var1': 'new_var1',
        'old_var2': Variable('dynamic_var2')
    }

@pytest.fixture
def replacer(variables):
    return VariablesReplacer(variables)

# Test initialization with a dictionary of variables
def test_initialization(variables):
    assert isinstance(VariablesReplacer(variables), VariablesReplacer)

# Test replacing module names in AST ImportFrom node
def test_replace_module_in_ast(replacer):
    node = ast.ImportFrom()
    node.module = 'some.module.name'
    replaced_node = replacer.visit_ImportFrom(node)