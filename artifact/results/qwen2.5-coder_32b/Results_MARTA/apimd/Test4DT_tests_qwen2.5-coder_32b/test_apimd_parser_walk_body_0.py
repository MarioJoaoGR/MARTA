
import pytest
from ast import parse, If, Try, Assign, Expr
from typing import Sequence, Iterator
from apimd.parser import walk_body

def test_none_input_handling():
    try:
        nodes = list(walk_body(None))  # type: ignore
    except TypeError as e:
        assert str(e) == "'NoneType' object is not iterable"





def test_assign_statement_handling():
    source_code = """
result = 10
"""
    tree = parse(source_code)
    nodes = list(walk_body(tree.body))
    assert isinstance(nodes[0], Assign)

def test_expr_statement_handling():
    source_code = """
print('Hello, World!')
"""
    tree = parse(source_code)
    nodes = list(walk_body(tree.body))
    assert isinstance(nodes[0], Expr)