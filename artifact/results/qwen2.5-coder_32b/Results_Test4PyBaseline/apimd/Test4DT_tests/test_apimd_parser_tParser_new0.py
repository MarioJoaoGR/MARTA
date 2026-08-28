
import pytest
from apimd.parser import Parser

def test_parser_default_initialization():
    p = Parser()
    assert p.link is True
    assert p.b_level == 1
    assert p.toc is False
    assert isinstance(p.level, dict) and not p.level
    assert isinstance(p.doc, dict) and not p.doc
    assert isinstance(p.docstring, dict) and not p.docstring
    assert isinstance(p.imp, dict) and not p.imp
    assert isinstance(p.root, dict) and not p.root
    assert isinstance(p.alias, dict) and not p.alias
    assert isinstance(p.const, dict) and not p.const

def test_parser_custom_initialization():
    p = Parser.new(link=False, level=2, toc=True)
    assert p.link is True  # Assuming link should be True if toc is True