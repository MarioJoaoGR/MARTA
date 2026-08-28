
import pytest
from ast import parse, ClassDef, AnnAssign, Assign, Delete, Name, expr, stmt
from apimd.parser import Parser

def get_class_node(source_code: str) -> ClassDef:
    tree = parse(source_code)
    for node in tree.body:
        if isinstance(node, ClassDef):
            return node
    raise ValueError("No class definition found in the source code")



def test_invalid_inputs():
    with pytest.raises(SyntaxError):
        source_code = """
class MyClass(
"""
        parse(source_code)


