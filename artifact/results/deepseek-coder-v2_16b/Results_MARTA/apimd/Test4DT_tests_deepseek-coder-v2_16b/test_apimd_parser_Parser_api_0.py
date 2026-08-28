
import pytest
from apimd.parser import Parser
from ast import FunctionDef, AsyncFunctionDef, ClassDef

def test_valid_input():
    p = Parser(link=True, level=1)
    pkg_content = 'sample code'
    with pytest.raises(TypeError):
        p.parse('pkg_name', pkg_content)

def test_edge_case_none():
    p = Parser(link=True, level=1)
    with pytest.raises(AttributeError):
        p.api('pkg_name', None, prefix='')

def test_invalid_input():
    p = Parser(link=True, level=1)
    with pytest.raises(AttributeError):
        p.api('invalid_pkg_name', 'sample code', prefix='')
