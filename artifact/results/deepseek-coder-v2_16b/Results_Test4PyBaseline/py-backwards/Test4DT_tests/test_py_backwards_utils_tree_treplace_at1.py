
import ast
from typing import List, Union
import pytest

def replace_at(index: int, parent: ast.AST, nodes: Union[ast.AST, List[ast.AST]]) -> None:
    """Replaces node in parents body at index with nodes."""
    if not isinstance(nodes, list):
        nodes = [nodes]
    
    parent.body[index:index+1] = nodes  # type: ignore

# Test cases for replace_at function
def test_replace_at_single_node():
    code = "def example():\n    pass"
    tree = ast.parse(code)
    assign_node1 = ast.parse("x = 1").body[0]
    replace_at(1, tree.body[0], assign_node1)
    assert len(tree.body[0].body) == 2
    assert isinstance(tree.body[0].body[1], type(assign_node1))

def test_replace_at_multiple_nodes():
    code = "def example():\n    pass"
    tree = ast.parse(code)
    assign_node1 = ast.parse("x = 1").body[0]
    assign_node2 = ast.parse("y = 2").body[0]
    replace_at(1, tree.body[0], [assign_node1, assign_node2])