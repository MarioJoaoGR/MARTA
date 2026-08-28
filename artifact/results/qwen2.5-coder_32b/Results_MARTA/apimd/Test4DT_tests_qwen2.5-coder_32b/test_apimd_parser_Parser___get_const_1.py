
import pytest
from apimd.parser import Parser

def setup_parser_with_constants():
    p = Parser()
    script = """
# Module: module.name

CONSTANT1 = 42
CONSTANT2 = 'Hello, World!'
"""
    p.parse('module.name', script)
    return p

def setup_parser_without_constants():
    p = Parser()
    script = """
# Empty Module

No constants here.
"""
    p.parse('empty.module', script)
    return p



def test_module_not_found():
    parser = setup_parser_with_constants()
    result = parser._Parser__get_const('nonexistent.module')
    assert result == ""