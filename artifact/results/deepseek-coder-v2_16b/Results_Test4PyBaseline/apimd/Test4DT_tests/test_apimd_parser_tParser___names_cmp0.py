
# Module: apimd.parser
import pytest
from apimd.parser import Parser

# Test creating a Parser instance without parameters
def test_create_parser_without_parameters():
    p = Parser()
    assert isinstance(p, Parser)
    assert p.link is True
    assert p.b_level == 1
    assert p.toc is False
    assert isinstance(p.level, dict)
    assert isinstance(p.doc, dict)
    assert isinstance(p.docstring, dict)
    assert isinstance(p.imp, dict)
    assert isinstance(p.root, dict)
    assert isinstance(p.alias, dict)