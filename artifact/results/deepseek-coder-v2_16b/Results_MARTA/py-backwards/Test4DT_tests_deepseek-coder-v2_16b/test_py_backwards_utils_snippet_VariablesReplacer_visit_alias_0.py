
import pytest
from py_backwards.utils.snippet import VariablesReplacer
from typing import Dict, List

class Variable:
    def __init__(self, value):
        self.value = value

@pytest.fixture
def variables_dict():
    return {
        'old_module': Variable('new_module')
    }

@pytest.fixture
def replacer(variables_dict):
    return VariablesReplacer(variables_dict)

class ASTNode:
    def __init__(self):
        self.name = 'old_module'

class ASTAlias:
    def __init__(self):
        self.asname = 'old_alias'


def test_replace_field_or_node(replacer, variables_dict):
    alias_node = ASTAlias()
    replaced_alias = replacer._replace_field_or_node(alias_node, 'asname', all_types=True)
    assert isinstance(replaced_alias, ASTAlias)
