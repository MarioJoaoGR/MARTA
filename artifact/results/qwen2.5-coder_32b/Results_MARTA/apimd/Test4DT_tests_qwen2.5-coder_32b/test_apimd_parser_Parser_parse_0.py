
import pytest
from apimd.parser import Parser

def test_happy_path():
    p = Parser()
    script_content = 'def test_func(): pass'
    p.parse('pkg_name', script_content)
    assert 'pkg_name' in p.doc, "Module name should be in doc dictionary"
    assert p.level['pkg_name'] == 0, "Level should be 0 for top-level module"

def test_edge_cases():
    p = Parser()
    script_content = ''
    p.parse('pkg_name', script_content)
    assert 'pkg_name' in p.doc, "Module name should be in doc dictionary even with empty script"
    assert p.level['pkg_name'] == 0, "Level should be 0 for top-level module with empty script"

def test_invalid_inputs():
    p = Parser()
    script_content = 12345
    with pytest.raises(TypeError):
        p.parse('pkg_name', script_content)
