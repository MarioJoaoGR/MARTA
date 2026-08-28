
# Module: apimd.parser
# test_parser.py
from apimd.parser import Parser
from ast import parse
import pytest

@pytest.mark.skip(reason="Unparse module is not available")
def test_globals_with_annassign():
    p = Parser()
    node = parse("""
        class Example:
            x: int = 1
    """)
    p.globals(root="example_package", node=node)
    
    assert "x" in p.alias
    assert p.alias["x"] == "int"
    assert "x" in p.const
    assert p.const["x"] == "int"
    assert "example_package" in p.root