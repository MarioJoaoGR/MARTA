
import pytest
from apimd.parser import Parser

def test_valid_input_default_init():
    p = Parser()
    assert hasattr(p, 'link')
    assert hasattr(p, 'b_level')
    assert hasattr(p, 'toc')
    assert p.link == True
    assert p.b_level == 1
    assert p.toc == False

def test_valid_input_parameterized_init():
    p = Parser(link=True, b_level=1, toc=False)
    assert hasattr(p, 'link')
    assert hasattr(p, 'b_level')
    assert hasattr(p, 'toc')
    assert p.link == True
    assert p.b_level == 1
    assert p.toc == False

def test_valid_input_parameterized_init_with_toc():
    p = Parser(link=True, b_level=1, toc=True)
    assert hasattr(p, 'link')
    assert hasattr(p, 'b_level')
    assert hasattr(p, 'toc')
    assert p.link == True
    assert p.b_level == 1
    assert p.toc == True
