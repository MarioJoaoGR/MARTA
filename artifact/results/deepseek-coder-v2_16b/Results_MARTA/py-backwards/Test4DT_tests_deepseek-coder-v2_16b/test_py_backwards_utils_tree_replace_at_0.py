
import ast
from typing import List, Union
import pytest
from py_backwards.utils.tree import replace_at

def test_replace_valid():
    func_def = ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)
    tree = ast.parse('pass')
    replace_at(index=0, parent=tree, nodes=func_def)
    assert isinstance(tree.body[0], ast.FunctionDef)
    assert tree.body[0].name == 'new_func'

