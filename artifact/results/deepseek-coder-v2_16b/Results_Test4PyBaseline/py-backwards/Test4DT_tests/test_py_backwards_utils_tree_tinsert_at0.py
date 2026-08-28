
import ast
from typing import List, Union
import pytest

# Import the function from its module
from py_backwards.utils.tree import insert_at

def test_insert_single_node():
    code = "def example():\n    pass"
    tree = ast.parse(code)
    assign_node = ast.parse("x = 1").body[0]
    insert_at(2, tree.body[0], assign_node)
    expected_ast = ast.parse("def example():\n    pass\n    x = 1")
    assert ast.dump(tree) == ast.dump(expected_ast), f"Expected {ast.dump(expected_ast)}, but got {ast.dump(tree)}"

def test_insert_multiple_nodes():
    code = "def example():\n    pass"
    tree = ast.parse(code)
    assign_node1 = ast.parse("x = 1").body[0]
    assign_node2 = ast.parse("y = 2").body[0]
    insert_at(2, tree.body[0], [assign_node1, assign_node2])
    expected_ast = ast.parse("def example():\n    pass\n    x = 1\n    y = 2")