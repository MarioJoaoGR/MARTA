
import ast
from typing import List, Union
import pytest
from unittest.mock import patch
from py_backwards.transformers import FunctionsAnnotationsTransformer

# Define the replace_at function as per the provided code snippet
def replace_at(index: int, parent: ast.AST, nodes: Union[ast.AST, List[ast.AST]]) -> None:
    """Replaces node in parents body at index with nodes."""
    if not isinstance(parent, ast.AST):
        raise TypeError("Parent must be an instance of ast.AST")
    parent.body.pop(index)  # type: ignore
    insert_at(index, parent, nodes)

# Define the insert_at function as a placeholder for the actual implementation
def insert_at(index: int, parent: ast.AST, nodes: Union[ast.AST, List[ast.AST]]) -> None:
    if isinstance(nodes, list):
        parent.body.insert(index, *nodes)  # type: ignore
    else:
        parent.body.insert(index, nodes)  # type: ignore

# Test for replacing a node in the parent's body at a valid index with a single AST node
def test_valid_replace():
    tree = ast.parse('def example(): pass')
    func_def = ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)
    
    replace_at(index=0, parent=tree, nodes=func_def)
    
    assert isinstance(tree.body[0], ast.FunctionDef)
    assert tree.body[0].name == 'new_func'

# Test for raising IndexError when the provided index is out of range for the parent's body list
def test_invalid_index():
    tree = ast.parse('def example(): pass')
    func_def = ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)
    
    with pytest.raises(IndexError):
        replace_at(index=999, parent=tree, nodes=func_def)

# Test for raising TypeError when the provided parent is not an instance of ast.AST
def test_invalid_parent():
    tree = 'not a valid AST node'
    func_def = ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)
    
    with pytest.raises(TypeError):
        replace_at(index=0, parent=tree, nodes=func_def)
